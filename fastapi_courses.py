from fastapi import FastAPI, APIRouter, HTTPException, status
from pydantic import BaseModel, RootModel

app = FastAPI()

# Router with a common prefix and a tag for Swagger
courses_router = APIRouter(
    prefix="/api/v1/courses",  # Adds /api/v1/courses to every path in this router
    tags=["courses-service"]  # Groups the routes under the "courses-service" tag in the docs
)


class CourseIn(BaseModel):
    """
    Model for incoming data (course creation and update).
    """
    title: str  # Course title
    max_score: int  # Maximum score
    min_score: int  # Minimum passing score
    description: str  # Short course description


class CourseOut(CourseIn):
    """
    Model for outgoing data, including the course ID.
    """
    id: int  # Unique course identifier


class CoursesStore(RootModel):
    """
    In-memory courses storage used instead of a real database.
    """
    root: list[CourseOut]  # List of all courses

    def find(self, course_id: int) -> CourseOut | None:
        """
        Finds a course by ID.

        :param course_id: Course identifier.
        :return: CourseOut or None if the course is not found.
        """
        return next(filter(lambda course: course.id == course_id, self.root), None)

    def create(self, course_in: CourseIn) -> CourseOut:
        """
        Creates a new course and generates the next ID for it.

        The ID is based on the current maximum ID, so it stays unique
        even after courses have been deleted.

        :param course_in: Input data of the new course.
        :return: The created course with its ID.
        """
        next_id = max((course.id for course in self.root), default=0) + 1
        course = CourseOut(id=next_id, **course_in.model_dump())
        self.root.append(course)
        return course

    def update(self, course_id: int, course_in: CourseIn) -> CourseOut:
        """
        Updates an existing course by ID.

        :param course_id: Identifier of the course to update.
        :param course_in: New course data.
        :return: The updated course.
        """
        # Find the index of the existing record
        index = next(index for index, course in enumerate(self.root) if course.id == course_id)
        # Build a new object with the same ID and the updated fields
        updated = CourseOut(id=course_id, **course_in.model_dump())
        # Replace it in the list
        self.root[index] = updated
        return updated

    def delete(self, course_id: int) -> None:
        """
        Deletes a course by ID by filtering the list.

        :param course_id: Identifier of the course to delete.
        """
        self.root = [course for course in self.root if course.id != course_id]


# Initialize the storage with an empty list
store = CoursesStore(root=[])


@courses_router.get("/{course_id}", response_model=CourseOut)
async def get_course(course_id: int):
    """
    GET /api/v1/courses/{course_id}
    Returns a course by ID or 404 if it is not found.
    """
    if not (course := store.find(course_id)):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return course


@courses_router.get("", response_model=list[CourseOut])
async def get_courses():
    """
    GET /api/v1/courses
    Returns the list of all courses.
    """
    return store.root


@courses_router.post("", response_model=CourseOut, status_code=status.HTTP_201_CREATED)
async def create_course(course: CourseIn):
    """
    POST /api/v1/courses
    Creates a new course and returns its data with the ID.
    """
    return store.create(course)


@courses_router.put("/{course_id}", response_model=CourseOut)
async def update_course(course_id: int, course: CourseIn):
    """
    PUT /api/v1/courses/{course_id}
    Updates a course by ID or returns 404 if it does not exist.
    """
    if not store.find(course_id):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    return store.update(course_id, course)


@courses_router.delete("/{course_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_course(course_id: int):
    """
    DELETE /api/v1/courses/{course_id}
    Deletes a course by ID or returns 404 if it does not exist.
    """
    if not store.find(course_id):
        raise HTTPException(
            detail=f"Course with id {course_id} not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

    store.delete(course_id)
    # With status_code=204 the response body is empty


# Include the router in the main application
app.include_router(courses_router)

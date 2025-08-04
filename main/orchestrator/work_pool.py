from prefect.client.orchestration import get_client
from prefect.client.schemas.actions import WorkPoolCreate
import asyncio

async def create_work_pool():
    async with get_client() as client:
        try:
            await client.create_work_pool(
                work_pool=WorkPoolCreate(
                    name="my-docker-pool",
                    type="docker"
                )
            )
            print("Work pool 'my-docker-pool' created successfully")
        except Exception as e:
            print(f"Work pool creation failed or already exists: {e}")

if __name__ == "__main__":
    asyncio.run(create_work_pool())
import  motor.motor_asyncio

MONGODB_URL = 'mongodb://localhost:2701/test'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

#connect to the db

database = client.test
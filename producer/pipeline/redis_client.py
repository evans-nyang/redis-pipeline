import json
import os

import redis


class RedisClient:
    """
    Custom Redis client with all the wrapper functions.
    This client implements FIFO for the pipeline.
    """

    try:
        host = os.environ["MYHOST"]
        port = int(os.environ["PORT"])
        db = int(os.environ["DB"])
        connection = redis.Redis(host=host, port=port, db=db)
        key = "DATA-PIPELINE-KEY"
    except Exception as err:
        print("\nEncountered an exception during connection!")
        raise err

    def _convert_data_to_json(self, data):
        try:
            return json.dumps(data)
        except Exception as err:
            print(f"Failed to convert data into json, encountered error: {err}")
            raise err

    def _convert_data_from_json(self, data):
        try:
            return json.loads(data)
        except Exception as err:
            print(f"Failed to convert data into dict, encountered error: {err}")
            raise err

    def send_data_to_pipeline(self, data):
        data = self._convert_data_to_json(data)
        self.connection.lpush(self.key, data)

    def get_data_from_pipeline(self):
        try:
            data = self.connection.rpop(self.key)
            return self._convert_data_from_json(data)
        except Exception as err:
            print(f"Failed to get more data from pipeline with error: {err}")
            raise err

    def get_items_in_pipeline(self):
        return self.connection.llen(self.key)

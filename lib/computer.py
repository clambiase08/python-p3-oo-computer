class Computer:
    all = []

    def __init__(self, brand, model, memory_GB=8, storage_free=1000):
        self._brand = brand
        self._model = model
        self.memory_GB = memory_GB
        self.storage_free = storage_free
        Computer.all.append(self)

    @property
    def brand(self):
        return self._brand

    @property
    def model(self):
        return self._model

    @property
    def memory_GB(self):
        return self._memory_GB

    @memory_GB.setter
    def memory_GB(self, value):
        self._memory_GB = value
        return self._memory_GB

    @property
    def storage_free(self):
        return self._storage_free

    @storage_free.setter
    def storage_free(self, value):
        if 0 <= value <= 1000:
            self._storage_free = value
        return self._storage_free

    def upgrade_memory(self, RAM):
        self.memory_GB += RAM.get("size")
        return self.memory_GB

    def is_disk_full(self, file_size):
        return self.storage_free < file_size

    def save_file(self, file):
        total_space = sum(self._file.get("size"))
        if total_space > file.get("size"):
            self.storage_free -= file.get("size")
            return f"{file['name']} has been saved!"
        else:
            return f"There is not enough space on disk to save {file['name']}."

    def delete_file(self, file):
        self.storage_free += file.get("size")
        return f"{file['name']} has been deleted"

    def specs(self):
        return f"You have {self.storage_free}GB of storage space and {self.memory_GB}GB of disk space"

    @classmethod
    def brands(cls):
        return list(set([brand for brand in cls.all]))

    @classmethod
    def models(cls):
        return [*set([model for model in cls.all])]

    @classmethod
    def largest_memory(cls):
        return max(cls.all, key=lambda x: x.memory_GB)


if __name__ == "__main__":
    # you can write test code here
    # or in debug.py
    pass

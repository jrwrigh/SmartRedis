import os
import inspect
import numpy as np
import os.path as osp


from .dataset import Dataset
from .error import RedisConnectionError, RedisReplyError
from .silcPy import PyClient
from .util import Dtypes


class Client(PyClient):
    def __init__(self, cluster=False, fortran=False):
        """Initialize a RedisAI client.

        :param cluster: True if connecting to a redis cluster, defaults to False
        :type cluster: bool, optional
        :param fortran: True if using Fortran arrays, defaults to False
        :type fortran: bool, optional
        :raises RedisConnectionError: if connection initialization fails
        """
        if "SSDB" not in os.environ:
            raise RedisConnectionError()
        try:
            super().__init__(cluster, fortran)
        except RuntimeError as e:
            raise RedisConnectionError(str(e))

    def put_tensor(self, key, data):
        """Put a tensor to a Redis database

        :param key: key for tensor for be stored at
        :type key: str
        :param data: numpy array
        :type data: np.array
        :raises RedisReplyError: if put fails
        """
        if not isinstance(data, np.ndarray):
            raise TypeError("Argument provided was not a numpy array")
        dtype = Dtypes.tensor_from_numpy(data)
        try:
            super().put_tensor(key, dtype, data)
        except RuntimeError as e:
            raise RedisReplyError(str(e), "put_tensor") from None

    def get_tensor(self, key):
        """Get a tensor from the database

        :param key: key to get tensor from
        :type key: str
        :raises RedisReplyError: if get fails
        :return: numpy array
        :rtype: np.array
        """
        try:
            return super().get_tensor(key)
        except RuntimeError as e:
            raise RedisReplyError(str(e), "get_tensor") from None

    def put_dataset(self, dataset):
        """Put a Dataset instance into the database

        All associated tensors and metadata within the Dataset
        instance will also be stored

        :param dataset: a Dataset instance
        :type dataset: Dataset
        :raises TypeError: if argument is not a Dataset
        :raises RedisReplyError: if connection fails
        """
        if not isinstance(dataset, Dataset):
            raise TypeError("Argument to put_dataset was not of type Dataset")
        try:
            super().put_dataset(dataset)
        except RuntimeError as e:
            raise RedisReplyError(str(e), "put_dataset") from None

    def get_dataset(self, key):
        """Get a dataset from the database

        :param key: key the dataset is stored under
        :type key: str
        :raises RedisConnectionError: if connection fails
        :return: Dataset instance
        :rtype: Dataset
        """
        try:
            dataset = super().get_dataset(key)
            return dataset
        except RuntimeError as e:
            raise RedisReplyError(str(e), "get_dataset", key=key) from None

    def set_function(self, key, function, device="CPU"):
        """Set a callable function into the database

        Function must be a callable TorchScript function and have at least
        one input and one output. Call the function with the Client.run_script
        method.
        Device selection is either "GPU" or "CPU". If many devices are

        present, a number can be passed for specification e.g. "GPU:1"

        :param key: key to store function at
        :type key: str
        :param function: callable function
        :type function: callable
        :param device: device to run function on, defaults to "CPU"
        :type device: str, optional
        :raises TypeError: if argument was not a callable function
        :raises RedisReplyError: if function failed to set
        """
        device = self.__check_device(device)
        if not callable(function):
            raise TypeError("Argument provided was not a callable function")
        fn_src = inspect.getsource(function)
        try:
            super().set_script(key, device, fn_src)
        except RuntimeError as e:
            raise RedisReplyError(str(e), "set_function") from None

    def set_script(self, key, script, device="CPU"):
        """Store a TorchScript at key in database

        Device selection is either "GPU" or "CPU". If many devices are
        present, a number can be passed for specification e.g. "GPU:1"

        :param key: key to store script under
        :type key: str
        :param script: TorchScript code
        :type script: str
        :param device: device for script execution, defaults to "CPU"
        :type device: str, optional
        :raises RedisReplyError: if script fails to set
        """
        device = self.__check_device(device)
        try:
            super().set_script(key, device, script)
        except RuntimeError as e:
            raise RedisReplyError(str(e), "set_script") from None

    def set_script_from_file(self, key, file, device="CPU"):
        """Same as Client.set_script but from file
        :param key: key to store script under
        :type key: str
        :param file: path to TorchScript code
        :type file: str
        :param device: device for script execution, defaults to "CPU"
        :type device: str, optional
        :raises RedisReplyError: if script fails to set
        """
        device = self.__check_device(device)
        file_path = self.__check_file(file)
        try:
            super().set_script_from_file(key, device, file_path)
        except RuntimeError as e:
            raise RedisReplyError(str(e), "set_script_from_file") from None

    def get_script(self, key):
        """Get a Torchscript stored in the database

        :param key: key at which script is stored
        :type key: str
        :raises RedisReplyError: if script doesn't exist
        :return: TorchScript stored at key
        :rtype: str
        """
        try:
            script = super().get_script(key)
            return script
        except RuntimeError as e:
            raise RedisReplyError(str(e), "get_script") from None

    def run_script(self, key, fn_name, inputs, outputs):
        """Execute TorchScript stored inside the databse remotely

        :param key: key script is stored under
        :type key: str
        :param fn_name: name of the function within the script to execute
        :type fn_name: str
        :param inputs: list of input tensors stored in database
        :type inputs: list[str]
        :param outputs: list of output tensor names to store results under
        :type outputs: list[str]
        :raises RedisReplyError: if script execution fails
        """
        try:
            super().run_script(key, fn_name, inputs, outputs)
        except RuntimeError as e:
            raise RedisReplyError(str(e), "run_script") from None

    @staticmethod
    def __check_file(file):
        file_path = osp.abspath(file)
        if not osp.isfile(file_path):
            raise FileNotFoundError(file_path)
        return file_path

    @staticmethod
    def __check_device(device):
        device = device.upper()
        if not device.startswith("CPU") and not device.startswith("GPU"):
            raise TypeError("Device argument must start with either CPU or GPU")
        return device

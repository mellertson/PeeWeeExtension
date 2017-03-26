from datetime import datetime
import peewee as pw
from MoneyMaker.Database import MySQL_BaseModel

MAX_LINUX_FILENAME = 255

class HTMModel(MySQL_BaseModel):
    """
    Data model for HTM Models, as contained in five files.
    """
    id = pw.PrimaryKeyField()
    name = pw.FixedCharField(max_length=128)
    created = pw.DateTimeField(default=datetime.now)
    # base description
    base_description_filename=pw.CharField(max_length=MAX_LINUX_FILENAME)
    base_description_file = pw.TextField()
    # permutations
    permutations_filename = pw.CharField(max_length=MAX_LINUX_FILENAME)
    permutations_file = pw.TextField()
    # description
    description_filename = pw.CharField(max_length=MAX_LINUX_FILENAME)
    description_file = pw.TextField()
    # model_params
    model_params_filename = pw.CharField(max_length=MAX_LINUX_FILENAME)
    model_params_file = pw.TextField()
    # params
    params_filename = pw.CharField(max_length=MAX_LINUX_FILENAME)
    params_file = pw.TextField()

    class Meta:
        order_by = ('name',)

    @classmethod
    def createModel(cls, name, base_description_filename, permutations_filename,
               description_filename, model_params_filename, params_filename):
        """
        Creates a record in the database for the HTM Model
        :param name: the name of the HTM model
        :param base_description_filename: 
        :param permutations_filename: 
        :param description_filename: 
        :param model_params_filename: 
        :param params_filename:
        """
        # read in contents of all five files in the model
        with open(base_description_filename, 'r') as bdFile:
            base_description_file = bdFile.read()
        with open(permutations_filename, 'r') as pFile:
            permutations_file = pFile.read()
        with open(description_filename, 'r') as dFile:
            description_file = dFile.read()
        with open(model_params_filename, 'r') as mpFile:
            model_params_file = mpFile.read()
        with open(params_filename, 'r') as pmsFile:
            params_file = pmsFile.read()

        # create the record in the database
        cls.create(
            name=name,
            base_description_filename=base_description_filename,
            permutations_filename=permutations_filename,
            description_filename=description_filename,
            model_params_filename=model_params_filename,
            params_filename=params_filename,
            base_description_file=base_description_file,
            permutations_file=permutations_file,
            description_file=description_file,
            model_params_file=model_params_file,
            params_file=params_file
            )
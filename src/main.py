from extract.extract import Extract
from transform.transform import run as transform
from load.load import Loader


extractor = Extract()
extractor.run()

transform()

loader = Loader()
loader.run()
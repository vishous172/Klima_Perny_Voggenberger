import xarray as xr
from glob import glob
import numpy as np
import pickle

#Path to Files from Kristofer Hasel
datapath="/raid/home/srvx7/lehre/users/a1401050/ERA5_data/*nc"
#make strings with all the filenames
filenames=glob(datapath)
#open one file to get the dimensions
infofile=xr.open_dataset(filenames[0])
#open data
file=xr.concat([xr.open_dataset(path,chunks=infofile.dims) for path in filenames],dim="time")

#create smaller file -> latitude and longitude: only 3 points for each
small_file=file.sel(latitude=np.arange(46,49),longitude=np.arange(11,14))
#calculate daily means from hourly data
small_daily_file=small_file.resample(time="1D").mean("time")

#save small-daily-data
pickle.dump(small_daily_file, open("/raid/home/srvx7/lehre/users/a1400416/ipython/Klima_Projekt/Daten/small_daily_data.p", "wb"))

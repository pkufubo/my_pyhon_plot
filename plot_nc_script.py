import numpy as np
import matplotlib.pylab as plt
import xarray as xr
import cartopy.crs as ccrs
##########
filepath = 'D:/CMIP6_test/'
filename = 'tas_Amon_BCC-ESM1_histSST_r1i1p1f1_gn_185001-201412.nc'
ds = xr.open_dataset(filepath+filename)
#########
fig = plt.figure(figsize=(8, 10))

# Label axes of a Plate Carree projection with a central longitude of 180:
ax1 = fig.add_subplot(1, 1, 1,
                      projection=ccrs.PlateCarree(central_longitude=180))

temp=ds['tas'].isel(time=-1)-273.15
temp.plot(ax=ax1,cbar_kwargs={'shrink':0.35, 'label': '$^{\circ}$C'})
#temp.plot(ax=ax1, cmap=WhGrYlRd,cbar_kwargs={'shrink': 0.5, 'label': '$^{\circ}$C'})

ax1.set_global()
ax1.coastlines()
ax1.gridlines(linestyle='--')

ax1.set_xticks([0, 60, 120, 180, -60, -120, -180], crs=ccrs.PlateCarree())
ax1.set_yticks([-90, -60, -30, 0, 30, 60, 90], crs=ccrs.PlateCarree())
ax1.set_xticklabels(['0','60E','120E','180','60W','120W','180'])
ax1.set_yticklabels(['90S','60S','30S','0','30N','60N','90N'])

ax1.set_title('Near-Surface Air Temperature')
ax1.set_xlabel('')
ax1.set_ylabel('')

fig.savefig('test.png',dpi=600)

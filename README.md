# Project: icepyx4gedi

## Introduction

The Global Ecosystem Dynamics Investigation (GEDI) is a full waveform LiDAR instrument aboard the International Space Station developed by NASA specifically optimized for measuring forest structure at a global scale. The Ice, Cloud, and Land Elevation Satellite-2 (ICESat-2) measures the height of a changing Earth via the ATLAS instrument which is optimized to measure changes in Earth's polar sea ice and land ice. However, ICESat-2 also collects elevation data over all surfaces from pole to pole. These data can be used together to map biophysical characteristics of ecosystems more completely and give scientists a better understanding of how these characteristics influence the global carbon cycle. By creating tools and utilities that access and work with both GEDI and ICESat-2 data using common routines, this work could lower barriers around working with these data together in activities like intercomparisons, fusion, and investigations that leverage synergies between the two sensors. 


### Collaborators

| Name | Personal goals | Can help with | Role |
| ------------- | ------------- | ------------- | ------------- |
|Aaron Friesz @amfriesz|...|...|...|
|Jessica Scheick @JessicaS11|...|...|...|
|Scott Henderson @scottyhq|...|...|...|
|Jack Hayes @Jack-Hayes|...|...|...|
|Zachary Fair @zachghiaccio|...|...|...|
|Wei Ji Leong @weiji14|...|...|...|
|H Rainak Khan Real @hrkreal|...|...|...|
|Francesca Lingo @f-lingo|...|...|...|
|Chao Wang @ChaoEcohydroRS|...|...|...|
|Romina Piunno @RomiP|...|...|...|
|Mikala Beig @mikala-nsidc|...|...|...|
|Tasha Snow @tsnow3|...|...|...|
|Aimee Barciauskas @abarciauskas-bgse|...|...|...|



### The Problem

The file size, dataset nuances, and hierarchical file structure of GEDI and ICESat-2 data files make working with these data daunting and difficult. To work with both GEDI and ICESat-2 data one must develop separate workflows to access and work with these data.


## Data & Tools

### Data

We will focus on the footprint data products, not the gridded data products. The specific data products are listed below.

- GEDI L1B Geolocated Waveform Data Global Footprint Level ([GEDI01_B v002](https://doi.org/10.5067/GEDI/GEDI01_B.002)) 
- GEDI L2A Elevation and Height Metrics Data Global Footprint Level ([GEDI02_A v002](https://doi.org/10.5067/GEDI/GEDI02_A.002)) 
- GEDI L2B Canopy Cover and Vertical Profile Metrics Data Global Footprint Level ([GEDI02_B v002](https://doi.org/10.5067/GEDI/GEDI02_B.002))

### Tools

- [h5py](https://docs.h5py.org/en/stable/) - has historically been the library used to read GEDI footprint data into Python.
- [icepyx](https://icepyx.readthedocs.io/en/latest/) - "shared library of resources - including existing resources, new code, tutorials, and use-cases/examples - that simplify the process of querying, obtaining, analyzing, and manipulating ICESat-2 and (via the QUEST module) relevant ancillary datasets to enable scientific discovery." The icepyx Developers. icepyx [Computer software](https://github.com/icesat2py/icepyx)
- [xarray](https://docs.xarray.dev/en/stable/)
- [Dask](https://docs.dask.org/en/stable/)
- GitHub

### Resources

Below are links to resources (i.e., tutorials, scripts, packages, and repos) that may be useful for context or for learning to work with GEDI footprint data.

- https://github.com/nasa/GEDI-Data-Resources/tree/main
- https://github.com/ornldaac/gedi_tutorials
- https://github.com/carlos-alberto-silva/rGEDI
- https://github.com/EduinHSERNA/pyGEDI
- https://github.com/icesat2py/icepyx/blob/gedi/doc/source/example_notebooks/GEDI_play.ipynb
- https://github.com/aestovall/GEDI_Workshop
- https://github.com/search?q=repo%3ASlideRuleEarth%2Fsliderule-python%20gedi%20&type=code

## Project Goals & Tasks

### Goals

This project aims to create and/or extend methods and routines in the [`icepyx`](https://icepyx.readthedocs.io/en/latest/) Python library to support GEDI footprint data products.

### Contributions

Work and contribution can be added to the [forked icepyx repo](https://github.com/ICESAT-2HackWeek/icepyx) in the [ICESAT-2HackWeek org](https://github.com/ICESAT-2HackWeek). If you are participants want to create a fork to their own GitHub space and check in contributions there, that is fine as well. 

### Tasks

Below are the list of features to be integrated into the `icepyx` Python library

- [ ] Search and discover GEDI footprint data from Earthdata Cloud
- [ ] Read GEDI footprint data into an xarray object
- [ ] Find concurrent/intersecting ICESat-2 and GEDI data files 
- [ ] GEDI quality filtering methods
- [ ] GEDI footprint to grid conversion
- [ ] Methods that make static and interactive plots for (stretch goal)
- [ ] Method to reduce the vertical step size (L2b) (stretch goal)

## Project Results

![Sticky notes of ideas to work on for the icepyx4gedi project](https://github.com/user-attachments/assets/22f1f7bc-e08e-4108-aa5a-13f849f9d894)

See issues, pull requests and the project board at:
- https://github.com/ICESAT-2HackWeek/icepyx/issues?q=is%3Aissue
- https://github.com/ICESAT-2HackWeek/icepyx/pulls?q=is%3Apr
- https://github.com/orgs/ICESAT-2HackWeek/projects/12/views/2

Summary points:
- Completed:
  - Determine spatial and temporal domain for development ([#4](https://github.com/ICESAT-2HackWeek/icepyx/issues/4))
  - Determine how to read-in GEDI L2b from Earthdata Cloud into at xarray dataset ([#3](https://github.com/ICESAT-2HackWeek/icepyx/issues/3))
  - Visualize GEDI L2b and ATL08 using lonboard ([#7](https://github.com/ICESAT-2HackWeek/icepyx/issues/7))
  - Determine how to discover variables from the Harmony API ([#19](https://github.com/ICESAT-2HackWeek/icepyx/issues/19))
- In progress (to be continued after hackweek and upstreamed into icepyx):
  - Read-in or translate GEDI L2B data to geoparquet ([#2](https://github.com/ICESAT-2HackWeek/icepyx/issues/2))
  - Search integration into icepyx ([#5](https://github.com/ICESAT-2HackWeek/icepyx/issues/5))
  - Data access integration into icepyx ([#6](https://github.com/ICESAT-2HackWeek/icepyx/issues/6))
  - Create a workflow for identifying coincident ICESat-2 x GEDI footprints in an input AOI ([#1](https://github.com/ICESAT-2HackWeek/icepyx/issues/1))
  - Modify icepyx Variables module to handle GEDI variable structure ([#15](https://github.com/ICESAT-2HackWeek/icepyx/issues/15))

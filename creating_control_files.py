import re
# from getWeatherData import main_func

s = "CISO: nlat=42 slat=32 wlon=-124.75 elon=-113.5"

pattern = r'''^
    (\w+):
    \s+
    nlat=(-?\d+(?:\.\d+)?)
    \s+
    slat=(-?\d+(?:\.\d+)?)
    \s+
    wlon=(-?\d+(?:\.\d+)?)
    \s+
    elon=(-?\d+(?:\.\d+)?)
$'''


def create_file_str(nlat, slat, wlon, elon, param, level, product_index):
  products = [
    "Analysis/3-hour Forecast/6-hour Forecast/9-hour Forecast/12-hour Forecast/15-hour Forecast/18-hour Forecast/21-hour Forecast/24-hour Forecast/27-hour Forecast/30-hour Forecast/33-hour Forecast/36-hour Forecast/39-hour Forecast/42-hour Forecast/45-hour Forecast/48-hour Forecast/51-hour Forecast/54-hour Forecast/57-hour Forecast/60-hour Forecast/63-hour Forecast/66-hour Forecast/69-hour Forecast/72-hour Forecast/75-hour Forecast/78-hour Forecast/81-hour Forecast/84-hour Forecast/87-hour Forecast/90-hour Forecast/93-hour /96-hour Forecast/99-hour Forecast/102-hour Forecast/105-hour Forecast/108-hour Forecast/111-hour Forecast/114-hour Forecast/117-hour Forecast/120-hour Forecast/123-hour Forecast/126-hour Forecast/129-hour Forecast/132-hour Forecast/135-hour Forecast/138-hour Forecast/141-hour Forecast/144-hour Forecast/147-hour Forecast/150-hour Forecast/153-hour Forecast/156-hour Forecast/159-hour Forecast/162-hour Forecast/165-hour Forecast/168-hour Forecast",
    "3-hour Average (initial+0 to initial+3)/6-hour Average (initial+0 to initial+6)/3-hour Average (initial+6 to initial+9)/6-hour Average (initial+6 to initial+12)/3-hour Average (initial+12 to initial+15)/6-hour Average (initial+12 to initial+18)/3-hour Average (initial+18 to initial+21)/6-hour Average (initial+18 to initial+24)/3-hour Average (initial+24 to initial+27)/6-hour Average (initial+24 to initial+30)/3-hour Average (initial+30 to initial+33)/6-hour Average (initial+30 to initial+36)/3-hour Average (initial+36 to initial+39)/6-hour Average (initial+36 to initial+42)/3-hour Average (initial+42 to initial+45)/6-hour Average (initial+42 to initial+48)/3-hour Average (initial+48 to initial+51)/6-hour Average (initial+48 to initial+54)/3-hour Average (initial+54 to initial+57)/6-hour Average (initial+54 to initial+60)/3-hour Average (initial+60 to initial+63)/6-hour Average (initial+60 to initial+66)/3-hour Average (initial+66 to initial+69)/6-hour Average (initial+66 to initial+72)/3-hour Average (initial+72 to initial+75)/6-hour Average (initial+72 to initial+78)/3-hour Average (initial+78 to initial+81)/6-hour Average (initial+78 to initial+84)/3-hour Average (initial+84 to initial+87)/6-hour Average (initial+84 to initial+90)/3-hour Average (initial+90 to initial+93)/6-hour Average (initial+90 to initial+96)/3-hour Average (initial+96 to initial+99)/6-hour Average (initial+96 to initial+102)/3-hour Average (initial+102 to initial+105)/6-hour Average (initial+102 to initial+108)/3-hour Average (initial+108 to initial+111)/6-hour Average (initial+108 to initial+114)/3-hour Average (initial+114 to initial+117)/6-hour Average (initial+114 to initial+120)/3-hour Average (initial+120 to initial+123)/6-hour Average (initial+120 to initial+126)/3-hour Average (initial+126 to initial+129)/6-hour Average (initial+126 to initial+132)/3-hour Average (initial+132 to initial+135)/6-hour Average (initial+132 to initial+138)/3-hour Average (initial+138 to initial+141)/6-hour Average (initial+138 to initial+144)/3-hour Average (initial+144 to initial+147)/6-hour Average (initial+144 to initial+150)/3-hour Average (initial+150 to initial+153)/6-hour Average (initial+150 to initial+156)/3-hour Average (initial+156 to initial+159)/6-hour Average (initial+156 to initial+162)/3-hour Average (initial+162 to initial+165)/6-hour Average (initial+162 to initial+168)",
    "3-hour Accumulation (initial+0 to initial+3)/6-hour Accumulation (initial+0 to initial+6)/3-hour Accumulation (initial+6 to initial+9)/6-hour Accumulation (initial+6 to initial+12)/3-hour Accumulation (initial+12 to initial+15)/6-hour Accumulation (initial+12 to initial+18)/3-hour Accumulation (initial+18 to initial+21)/6-hour Accumulation (initial+18 to initial+24)/3-hour Accumulation (initial+24 to initial+27)/6-hour Accumulation (initial+24 to initial+30)/3-hour Accumulation (initial+30 to initial+33)/6-hour Accumulation (initial+30 to initial+36)/3-hour Accumulation (initial+36 to initial+39)/6-hour Accumulation (initial+36 to initial+42)/3-hour Accumulation (initial+42 to initial+45)/6-hour Accumulation (initial+42 to initial+48)/3-hour Accumulation (initial+48 to initial+51)/6-hour Accumulation (initial+48 to initial+54)/3-hour Accumulation (initial+54 to initial+57)/6-hour Accumulation (initial+54 to initial+60)/3-hour Accumulation (initial+60 to initial+63)/6-hour Accumulation (initial+60 to initial+66)/3-hour Accumulation (initial+66 to initial+69)/6-hour Accumulation (initial+66 to initial+72)/3-hour Accumulation (initial+72 to initial+75)/6-hour Accumulation (initial+72 to initial+78)/3-hour Accumulation (initial+78 to initial+81)/6-hour Accumulation (initial+78 to initial+84)/3-hour Accumulation (initial+84 to initial+87)/6-hour Accumulation (initial+84 to initial+90)/3-hour Accumulation (initial+90 to initial+93)/6-hour Accumulation (initial+90 to initial+96)/3-hour Accumulation (initial+96 to initial+99)/6-hour Accumulation (initial+96 to initial+102)/3-hour Accumulation (initial+102 to initial+105)/6-hour Accumulation (initial+102 to initial+108)/3-hour Accumulation (initial+108 to initial+111)/6-hour Accumulation (initial+108 to initial+114)/3-hour Accumulation (initial+114 to initial+117)/6-hour Accumulation (initial+114 to initial+120)/3-hour Accumulation (initial+120 to initial+123)/6-hour Accumulation (initial+120 to initial+126)/3-hour Accumulation (initial+126 to initial+129)/6-hour Accumulation (initial+126 to initial+132)/3-hour Accumulation (initial+132 to initial+135)/6-hour Accumulation (initial+132 to initial+138)/3-hour Accumulation (initial+138 to initial+141)/6-hour Accumulation (initial+138 to initial+144)/3-hour Accumulation (initial+144 to initial+147)/6-hour Accumulation (initial+144 to initial+150)/3-hour Accumulation (initial+150 to initial+153)/6-hour Accumulation (initial+150 to initial+156)/3-hour Accumulation (initial+156 to initial+159)/6-hour Accumulation (initial+156 to initial+162)/3-hour Accumulation (initial+162 to initial+165)/6-hour Accumulation (initial+162 to initial+168)",
  ]
  output = f"dataset=ds084.1\ndate=202101010000/to/202212310000\ndatetype=init\nparam={param}\nlevel={level}\nnlat={nlat}\nslat={slat}\nwlon={wlon}\nelon={elon}  \nproduct={products[product_index]}\ntargetdir=/glade/scratch\n"
  return output
# product=Analysis/3-hour Forecast/6-hour Forecast/9-hour Forecast/12-hour Forecast/15-hour Forecast/18-hour Forecast/21-hour Forecast/24-hour Forecast/27-hour Forecast/30-hour Forecast/33-hour Forecast/36-hour Forecast/39-hour Forecast/42-hour Forecast/45-hour Forecast/48-hour Forecast/51-hour Forecast/54-hour Forecast/57-hour Forecast/60-hour Forecast/63-hour Forecast/66-hour Forecast/69-hour Forecast/72-hour Forecast/75-hour Forecast/78-hour Forecast/81-hour Forecast/84-hour Forecast/87-hour Forecast/90-hour Forecast/93-hour /96-hour Forecast/99-hour Forecast/102-hour Forecast/105-hour Forecast/108-hour Forecast/111-hour Forecast/114-hour Forecast/117-hour Forecast/120-hour Forecast/123-hour Forecast/126-hour Forecast/129-hour Forecast/132-hour Forecast/135-hour Forecast/138-hour Forecast/141-hour Forecast/144-hour Forecast/147-hour Forecast/150-hour Forecast/153-hour Forecast/156-hour Forecast/159-hour Forecast/162-hour Forecast/165-hour Forecast/168-hour Forecast
# product=3-hour Average (initial+0 to initial+3)/6-hour Average (initial+0 to initial+6)/3-hour Average (initial+6 to initial+9)/6-hour Average (initial+6 to initial+12)/3-hour Average (initial+12 to initial+15)/6-hour Average (initial+12 to initial+18)/3-hour Average (initial+18 to initial+21)/6-hour Average (initial+18 to initial+24)/3-hour Average (initial+24 to initial+27)/6-hour Average (initial+24 to initial+30)/3-hour Average (initial+30 to initial+33)/6-hour Average (initial+30 to initial+36)/3-hour Average (initial+36 to initial+39)/6-hour Average (initial+36 to initial+42)/3-hour Average (initial+42 to initial+45)/6-hour Average (initial+42 to initial+48)/3-hour Average (initial+48 to initial+51)/6-hour Average (initial+48 to initial+54)/3-hour Average (initial+54 to initial+57)/6-hour Average (initial+54 to initial+60)/3-hour Average (initial+60 to initial+63)/6-hour Average (initial+60 to initial+66)/3-hour Average (initial+66 to initial+69)/6-hour Average (initial+66 to initial+72)/3-hour Average (initial+72 to initial+75)/6-hour Average (initial+72 to initial+78)/3-hour Average (initial+78 to initial+81)/6-hour Average (initial+78 to initial+84)/3-hour Average (initial+84 to initial+87)/6-hour Average (initial+84 to initial+90)/3-hour Average (initial+90 to initial+93)/6-hour Average (initial+90 to initial+96)/3-hour Average (initial+96 to initial+99)/6-hour Average (initial+96 to initial+102)/3-hour Average (initial+102 to initial+105)/6-hour Average (initial+102 to initial+108)/3-hour Average (initial+108 to initial+111)/6-hour Average (initial+108 to initial+114)/3-hour Average (initial+114 to initial+117)/6-hour Average (initial+114 to initial+120)/3-hour Average (initial+120 to initial+123)/6-hour Average (initial+120 to initial+126)/3-hour Average (initial+126 to initial+129)/6-hour Average (initial+126 to initial+132)/3-hour Average (initial+132 to initial+135)/6-hour Average (initial+132 to initial+138)/3-hour Average (initial+138 to initial+141)/6-hour Average (initial+138 to initial+144)/3-hour Average (initial+144 to initial+147)/6-hour Average (initial+144 to initial+150)/3-hour Average (initial+150 to initial+153)/6-hour Average (initial+150 to initial+156)/3-hour Average (initial+156 to initial+159)/6-hour Average (initial+156 to initial+162)/3-hour Average (initial+162 to initial+165)/6-hour Average (initial+162 to initial+168)
# product=3-hour Accumulation (initial+0 to initial+3)/6-hour Accumulation (initial+0 to initial+6)/3-hour Accumulation (initial+6 to initial+9)/6-hour Accumulation (initial+6 to initial+12)/3-hour Accumulation (initial+12 to initial+15)/6-hour Accumulation (initial+12 to initial+18)/3-hour Accumulation (initial+18 to initial+21)/6-hour Accumulation (initial+18 to initial+24)/3-hour Accumulation (initial+24 to initial+27)/6-hour Accumulation (initial+24 to initial+30)/3-hour Accumulation (initial+30 to initial+33)/6-hour Accumulation (initial+30 to initial+36)/3-hour Accumulation (initial+36 to initial+39)/6-hour Accumulation (initial+36 to initial+42)/3-hour Accumulation (initial+42 to initial+45)/6-hour Accumulation (initial+42 to initial+48)/3-hour Accumulation (initial+48 to initial+51)/6-hour Accumulation (initial+48 to initial+54)/3-hour Accumulation (initial+54 to initial+57)/6-hour Accumulation (initial+54 to initial+60)/3-hour Accumulation (initial+60 to initial+63)/6-hour Accumulation (initial+60 to initial+66)/3-hour Accumulation (initial+66 to initial+69)/6-hour Accumulation (initial+66 to initial+72)/3-hour Accumulation (initial+72 to initial+75)/6-hour Accumulation (initial+72 to initial+78)/3-hour Accumulation (initial+72 to initial+81)/6-hour Accumulation (initial+78 to initial+84)/3-hour Accumulation (initial+84 to initial+87)/6-hour Accumulation (initial+84 to initial+90)/3-hour Accumulation (initial+90 to initial+93)/6-hour Accumulation (initial+90 to initial+96)/3-hour Accumulation (initial+96 to initial+99)/6-hour Accumulation (initial+96 to initial+102)/3-hour Accumulation (initial+102 to initial+105)/6-hour Accumulation (initial+102 to initial+108)/3-hour Accumulation (initial+108 to initial+111)/6-hour Accumulation (initial+108 to initial+114)/3-hour Accumulation (initial+114 to initial+117)/6-hour Accumulation (initial+114 to initial+120)/3-hour Accumulation (initial+120 to initial+123)/6-hour Accumulation (initial+120 to initial+126)/3-hour Accumulation (initial+126 to initial+129)/6-hour Accumulation (initial+126 to initial+132)/3-hour Accumulation (initial+132 to initial+135)/6-hour Accumulation (initial+132 to initial+138)/3-hour Accumulation (initial+138 to initial+141)/6-hour Accumulation (initial+138 to initial+144)/3-hour Accumulation (initial+144 to initial+147)/6-hour Accumulation (initial+144 to initial+150)/3-hour Accumulation (initial+150 to initial+153)/6-hour Accumulation (initial+150 to initial+156)/3-hour Accumulation (initial+156 to initial+159)/6-hour Accumulation (initial+156 to initial+162)/3-hour Accumulation (initial+162 to initial+165)/6-hour Accumulation (initial+162 to initial+168)

strings = ["CISO: nlat=42 slat=32 wlon=-124.75 elon=-113.5",
"PJM: nlat=43 slat=34.25 wlon=-91 elon=-73.5",
"ERCOT: nlat=36.5 slat=25.25 wlon=-104.5 elon=-93.25",
"ISNE: nlat=48 slat=40 wlon=-74.25 elon=-66.5",
"MISO: nlat=50.00 slat=28.50 wlon=-107.75 elon=-81.75",
"BPAT: nlat=49.50 slat=39.50 wlon=-125.25 elon=-105.50",
"SWPP: nlat=49.50 slat=30.25 wlon=-107.75 elon=-89.50",
"SOCO: nlat=35.50 slat=29.25 wlon=-90.50 elon=-80.25",
"FPL: nlat=31.25 slat=24.00 wlon=-83.50 elon=-79.50",
"NYISO: nlat=45.50 slat=40.00 wlon=-80.25 elon=-71.25",
"BANC: nlat=41.75 slat=37.00 wlon=-124.00 elon=-120.00",
"LDWP: nlat=38.00 slat=33.25 wlon=-119.00 elon=-117.00",
"TIDC: nlat=38.25 slat=36.75 wlon=-121.75 elon=-119.75",
"DUK: nlat=37.00 slat=33.00 wlon=-84.75 elon=-77.75",
"SC: nlat=35.25 slat=31.50 wlon=-82.75 elon=-78.00",
"SCEG: nlat=35.25 slat=31.50 wlon=-83.00 elon=-78.75",
"SPA: nlat=40.75 slat=34.25 wlon=-98.00 elon=-89.00",
"FMPP: nlat=30.75 slat=24.00 wlon=-83.00 elon=-79.50",
"FPC: nlat=31.25 slat=25.75 wlon=-86.50 elon=-80.00",
"TAL: nlat=31.25 slat=29.75 wlon=-84.75 elon=-83.50",
"TEC: nlat=29.00 slat=27.00 wlon=-83.25 elon=-81.25",
"AECI: nlat=41.75 slat=34.25 wlon=-98.50 elon=-88.50",
"LGEE: nlat=39.50 slat=36.00 wlon=-89.75 elon=-82.25",
"DOPD: nlat=49.50 slat=46.75 wlon=-120.75 elon=-118.25",
"GCPD: nlat=48.50 slat=46.25 wlon=-120.50 elon=-118.50",
"GRID: nlat=46.25 slat=44.75 wlon=-119.75 elon=-118.25",
"IPCO: nlat=47.25 slat=41.50 wlon=-120.50 elon=-111.00",
"NEVP: nlat=42.50 slat=34.50 wlon=-122.00 elon=-111.00",
"NWMT: nlat=49.50 slat=43.25 wlon=-116.50 elon=-103.50",
"PACE: nlat=45.50 slat=33.00 wlon=-115.75 elon=-104.25",
"PACW: nlat=47.50 slat=38.75 wlon=-124.75 elon=-115.75",
"PGE: nlat=46.50 slat=44.25 wlon=-124.25 elon=-121.25",
"PSCO: nlat=41.75 slat=35.75 wlon=-109.50 elon=-102.00",
"PSEI: nlat=49.50 slat=45.75 wlon=-123.75 elon=-119.75",
"SCL: nlat=48.25 slat=47.00 wlon=-123.00 elon=-121.75",
"TPWR: nlat=48.25 slat=45.75 wlon=-124.00 elon=-120.50",
"WACM: nlat=48.00  slat=35.50 wlon=-114.50 elon=-95.75",
"SOCO: nlat=35.50 slat=29.50 wlon=-90.50 elon=-80.25",
"AZPS: nlat=36.75 slat=30.75 wlon=-115.25 elon=-108.75",
"EPE: nlat=34.00  slat=26.75 wlon=-108.75 elon=-98.25",
"PNM: nlat=44.50 slat=30.75 wlon=-123.50 elon=-101.50",
"SRP: nlat=34.50 slat=32.00 wlon=-113.75 elon=-110.50",
"TEPC: nlat=36.75 slat=31.25 wlon=-115.25 elon=-110.00",
"WALC: nlat=44.00 slat=30.75 wlon=-124.25 elon=-105.00",
"TVA: nlat=38.00 slat=31.75 wlon=-90.75 elon=-81.25",
"AL: nlat=42.75 slat=39.50 wlon=19.25 elon=21.00",
"AT: nlat=49.00 slat=46.50 wlon=9.50 elon=17.00",
"BE: nlat=51.50 slat=49.50 wlon=2.50 elon=6.25",
"BG: nlat=44.25 slat=41.25 wlon=22.25 elon=28.50",
"HR: nlat=46.50 slat=42.50 wlon=13.75 elon=19.50",
"DK: nlat=57.75 slat=54.50 wlon=7.50 elon=13.25",
"EE: nlat=59.50 slat=57.50 wlon=23.25 elon=28.25",
"FI: nlat=70.00 slat=59.75 wlon=20.50 elon=31.50",
"FR: nlat=51.25 slat=42.25 wlon=-5.25 elon=8.25",
"DE: nlat=55.25 slat=47.25 wlon=5.75 elon=15",
"GR: nlat=41.75 slat=35.00 wlon=20.25 elon=26.50",
"HU: nlat=48.50 slat=45.75 wlon=16.25 elon=22.75",
"IE: nlat=55.25 slat=51.75 wlon=-10.00 elon=-6.00",
"IT: nlat=47.00 slat=36.50 wlon=6.75 elon=18.50",
"LV: nlat=58.00 slat=55.50 wlon=21.00 elon=28.25",
"LT: nlat=56.25 slat=54.00 wlon=21.00 elon=26.50",
"NL: nlat=53.50 slat=50.75 wlon=3.25 elon=7.00",
"PL: nlat=54.75 slat=49 wlon=14 elon=24",
"PT: nlat=42.75 slat=36.50 wlon=-10.00 elon=-5.75",
"RO: nlat=48.25 slat=43.75 wlon=20.25 elon=29.50",
"RS: nlat=46.25 slat=42.25 wlon=18.75 elon=23.00",
"SK: nlat=49.50 slat=47.75 wlon=16.75 elon=22.50",
"SI: nlat=46.75 slat=45.50 wlon=13.75  elon=16.50",
"ES: nlat=43.75 slat=36.00 wlon=-9.25 elon=3.50",
"SE: nlat=69 slat=55.25 wlon=11.25 elon=21.25",
"CH: nlat=47.75 slat=45.75 wlon=6.00 elon=10.50",
"CZ: nlat=51.00 slat=48.50 wlon=12.25 elon=18.75",
"GB: nlat=61 slat=49.75 wlon=-8.25 elon=2.25"]

locations = [] # (grid, nlat, slat, wlon, elon)

for s in strings:
  m = re.match(pattern, s, re.VERBOSE)
  if m:
      name, nlat, slat, wlon, elon = m.groups()
      # convert the numeric strings to floats if you need
      nlat, slat, wlon, elon = map(float, (nlat, slat, wlon, elon))
      print(name, nlat, slat, wlon, elon)
      tmp = (name, nlat, slat, wlon, elon)
      locations.append(tmp)
      # print(type(name), type(nlat), type(slat), type(wlon), type(elon))
  else:
    print(f"ERROR {s}")

weather_vars = [ # param, level, product_index
  ("U GRD/V GRD", "HTGL:10", 0, "wind"), # wind 
  ("TMP/DPT", "HTGL:2", 0, "temp"), # temp and dewpoint
  ("DSWRF", "SFC:0", 1, "dswrf"), # dswrf
  ("A PCP", "SFC:0", 2, "rain"), # total precipitation
]

grids = [grid for grid, nlat, slat, wlon, elon in locations]
# print(grids)
# exit()

for grid, nlat, slat, wlon, elon in locations:
  for param, level, product_index, weather_type in weather_vars:
    print(grid, weather_type)
    # print(weather_type)
    # continue
    file_txt = create_file_str(nlat, slat, wlon, elon, param, level, product_index)
    # print(file_txt)
    file_name = f"../control_files/{grid}_{weather_type}_control.ctl"
    with open(file_name, "w+") as f:
      f.write(file_txt)
    # exit()
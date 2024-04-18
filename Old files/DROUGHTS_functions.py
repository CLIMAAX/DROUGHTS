

## Functions ##

def load_nuts_json(json_path):
    # dependencies: json, urllib, geopandas, 
    while True:
        uh = urllib.request.urlopen(json_path)
        data = uh.read()
        break  
    gdf = gpd.GeoDataFrame.from_features(json.loads(data)["features"])
    return gdf


def calculate_monthly_threshold(x, m, col_idx):
    idx = (x['timing'].str.contains(m))
    mon_loc_subset = precip.iloc[idx[idx].index, col_idx]
    return(jenkspy.jenks_breaks(mon_loc_subset, n_classes = 2)[1])

def identify_monthly_drought(x, m, col_idx, thrs):
    idx = (x['timing'].str.contains(m))
    x.iloc[idx[idx].index, col_idx] = x.iloc[idx[idx].index, col_idx] < thrs
    return(x)

def identify_t_m(k, m):
    if 'Jan' in precip.iloc[k, 0]: 
        return(int(0))
    if 'Feb' in precip.iloc[k, 0]:
        return(int(1))
    if 'Mar' in precip.iloc[k, 0]:
        return(int(2))
    if 'Apr' in precip.iloc[k, 0]:
        return(int(3))
    if 'May' in precip.iloc[k, 0]:
        return(int(4))
    if 'Jun' in precip.iloc[k, 0]:
        return(int(5))
    if 'Jul' in precip.iloc[k, 0]:
        return(int(6))
    if 'Aug' in precip.iloc[k, 0]:
        return(int(7))
    if 'Sep' in precip.iloc[k, 0]:
        return(int(8))
    if 'Oct' in precip.iloc[k, 0]:
        return(int(9))
    if 'Nov' in precip.iloc[k, 0]:
        return(int(10))
    if 'Dec' in precip.iloc[k, 0]:
        return(int(11))

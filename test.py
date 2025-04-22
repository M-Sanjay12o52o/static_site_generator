def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    lists = 0
    for handles in all_handles:
        lists += 1
        for handle in handles:
            if brand_name in handle:
                count += 1

    print("lists: ", lists)
    print("count: ", count)

    average = count / lists * 8

    # average number of handles that contain the brand_name across all the lists. (all handles)
    return average


all_handles = [
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"],
]
brand_name = "cosmo"

result = get_avg_brand_followers(all_handles, brand_name)

print("result: ", result)
# expected output: 1.33

from pyzillow.pyzillow import ZillowWrapper, GetDeepSearchResults, GetUpdatedPropertyDetails

address = "6202 Maddingly Ln, League City, TX"
zipcode = "77573"
zillow_data = ZillowWrapper("X1-ZWz186bgq2hcsr_22g4o")

deep_search_response = zillow_data.get_deep_search_results(address, zipcode)
result = GetDeepSearchResults(deep_search_response)

print(result.zillow_id)
print(result.home_type)
print(result.home_detail_link)
print(result.latitude)
print(result.longitude)
print(result.tax_year)
print(result.tax_value)
print(result.year_built)
print(result.property_size)
print(result.home_size)
print(result.bathrooms)
print(result.bedrooms)
print(result.last_sold_date)
print(result.last_sold_price)
print(result.zestimate_amount)

#CHAPTER 3 https://media.readthedocs.org/pdf/pyzillow/latest/pyzillow.pdf
#zillow_id = "tylerwooten99"
#zillow_data = ZillowWrapper("X1-ZWz186bgq2hcsr_22g4o")
#updated_property_details_response = zillow_data.get_updated_property_details(zillow_id)
#result = GetUpdatedPropertyDetails(updated_property_details_response)

#print("\n\n\n Chapter 3 \n\n")

#print(result.photo_gallery)
#print(result.home_info)
#print(result.floor_material)
#print(result.num_floors)
#print(result.basement)
#print(result.roof)
#print(result.rooms)
#print(result.view)
#print(result.parking_type)
#print(result.neighborhood)
#print(result.school_district)

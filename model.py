from transformers import pipeline
# Load model directly (skin type detection)
# Use a pipeline as a high-level helper


# this returns array of 3 dictionaries, each dictionary hase 2 keys, first key is label which gives value --> oily, normal, dry
# 2nd key is score
# for skin classification
skin_model = pipeline("image-classification", model="dima806/skin_types_image_detection")
skin_result = skin_model('./testImages/normal2.jpg')
# print(skin_result[0]['label'])

# Level -1: clear skin
# Level 0: Occasional Spots
# Level 1: Mild Acne
# Level 2: Moderate Acne
# Level 3: Severe Acne
# Level 4: Very severe Acne
acne_model = pipeline("image-classification", model="imfarzanansari/skintelligent-acne")
acne_result = acne_model('./testImages/acne.jpg')
# print(acne_result[0]['label'])

# consolidating  results
results = {}
results['skin'] = skin_result[0]['label']
results['acne'] = acne_result[0]['label']

print(results)


import numpy as np
from scipy import spatial
from statistics import mean



class Similarity:
    
    def __init__(self, features):
        self.features = features

    def recommend(self, values, customer_feature1, customer_feature2, customer_feature3, customer_feature4, k1 = 4, k2=1, k3=1, k4=1) -> list:
        similarity_list = list()
        similarity_list_img_1 = list()
        similarity_list_img_2 = list()
        similarity_list_img_3 = list()
        final_result = list()
        for each_img in self.features:

            similarity_list.append(self.cosine_similarity(values, customer_feature1, self.avrage_point(each_img)))
            similarity_list_img_1.append(self.cosine_similarity(values, customer_feature1, self.avrage_point(each_img)))
            similarity_list_img_2.append(self.cosine_similarity(values, customer_feature1, self.avrage_point(each_img)))
            similarity_list_img_3.append(self.cosine_similarity(values, customer_feature1, self.avrage_point(each_img)))

        similarity_list = np.array(similarity_list)
        similarity_list_img_1 = np.array(similarity_list_img_1)
        similarity_list_img_2 = np.array(similarity_list_img_2)
        similarity_list_img_3 = np.array(similarity_list_img_3)

        final_result.append(np.argsort(similarity_list))
        final_result.append(np.argsort(similarity_list_img_1))
        final_result.append(np.argsort(similarity_list_img_2))
        final_result.append(np.argsort(similarity_list_img_3))

        return list(final_result)








    def recommend2(self, features, values, k):
        distance = np.array([self.distance_2(features, f, values) for f in self.features])
        k_indeces1 = np.argsort(distance)[:k]
        return k_indeces1


    def cosine_similarity(self, values: list, customer_feature: list, img_feature: list) -> float:
        weighted_array = values * customer_feature
        result = spatial.distance.cosine(weighted_array, img_feature)
        return result

    def avrage_point(self, img_src: list) -> list:
        final_list = []
        for each_img in img_src:
            final_list.append(mean(each_img))
        return final_list

    def distance_2(self, x, y, values):
        return np.sqrt(np.sum(values * ((x - y) ** 2))) 
    
    
    

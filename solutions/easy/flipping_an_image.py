class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            x = image[i][::-1]
            for j in range(len(x)):
                if x[j] == 0:
                    x[j] = x[j] ^ 1
                elif x[j] == 1:
                    x[j] = x[j] >> 1
            image[i] = x
        return image
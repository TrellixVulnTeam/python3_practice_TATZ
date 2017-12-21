class Restaurant:
    """定义餐厅类"""
    def __init__(self, name, res_type):
        self.name = name
        self.res_type = res_type

    def describe_restaurant(self):
        print('restaurant name is '+self.name + 'restaurant type is '+str(self.res_type))

    def open_restaurant(self):
        print('open restaurant'+self.name)


res1 = Restaurant('中餐馆', 1)
res2 = Restaurant('西餐馆', 2)

print(res1.name+"type is "+str(res1.res_type))
res2.open_restaurant()



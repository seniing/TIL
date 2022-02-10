from faker import Faker

# fake = Faker('ko_KR')
# Faker.seed(4321)

# print(fake.name())   # 이도윤

# fake2 = Faker('ko_KR')
# print(fake2.name())   # 이지후

fake = Faker('ko_KR')
fake.seed_instance(4321)

print(fake.name())   # 이도윤

fake2 = Faker('ko_KR')
print(fake2.name())   # (값이 바뀐다.)
# ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

# 1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
# 2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
# 3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
# 4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก(แสดงเพียง 1 ครั้ง)

# อธิบาย Input
# แบ่ง Data เป็น 2 ชุดด้วย /
#     -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
#     -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ



# class Data:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value

#     def __str__(self):
#         return "({0}, {1})".format(self.key, self.value)

# class hash:

#     # Code Here

class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)


class hash:
    def __init__(self, size, max_try):
        self.box = [""] * size
        self.size = size
        self.max_try = max_try
        self.count = 0
        #print("Size box ", len(self.box))
        #print("Type box ", type(self.box))

    def is_empty(self, idx):
        #print('temp', idx, self.box[idx])
        if idx >= self.size:
            return False
        return len(self.box[idx]) == 0

    def find_empty_box(self, org_idx):
        #F(i) = F(i-1) + 2*i - 1
        #print("Start at ", org_idx)
        t = [org_idx] * (self.size + 1)
        counter = 0
        while counter < self.max_try:
            if self.is_empty(t[counter]):
                #print("Found at", t[counter])
                return t[counter]
            counter += 1
            print("collision number", counter, "at", t[counter - 1])
            t[counter] = (t[counter - 1] + (2 * counter) - 1) % self.size
            #print(t)
        return -1

    def push(self, new):
        if self.count == self.size:
            self.print_()
        else:
            sum_as = self.sum_ascii(new) % self.size
            idx = self.find_empty_box(sum_as)
            if idx == -1:
                print("Max of collisionChain")
            else:
                self.box[idx] = ', '.join(new.split())
                #print('after added', self.box)
                self.count += 1
            self.print_()

    def is_full(self):
        return self.count == self.size

    def print_(self):
        for idx in range(self.size):
            print("#" + str(idx + 1) + "	", end='')
            if self.box[idx] != "":
                print("(" + self.box[idx] + ")")
            else:
                print("None")
        print("---------------------------")

    def sum_ascii(self, st):
        st = st.split()[0]
        return sum(ord(x) for x in st if x != ' ')


if __name__ == "__main__":
    inp_ = input(" ***** Fun with hashing *****\nEnter Input : ").split('/')
    l, mx = int(inp_[0].split()[0]), int(inp_[0].split()[1])
    _hash = hash(l, mx)
    for x in inp_[1].split(","):
        _hash.push(x)
        if _hash.is_full():
            print("This table is full !!!!!!")
            break
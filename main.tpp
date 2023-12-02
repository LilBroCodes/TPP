a=0;
b = 1;
tr = True;
fl = False;

print("a");
print(a);
print("b");
print(b);

if (tr == True) {
    print("tr");
} elif (fl == False) {
    print("fl");
} else {
    print("else");
}

a = 10;
a += 1;
a -= 1;
a *= 2;
a /= 2;

list = [1, 2, 3, 4, 5, 6, 7]

while (True) {
    print("Infinite loop");
}

for (i = 0; i < 5; i++) {
    print(i);
}

foreach (number in list) {
    print(number);
}

function add(a, b) {
    return a + b;
}

class MyClass {
    function init(this, args) {
        this.args = args;
    }
}

var obj = new MyClass(10);
print(obj.args);
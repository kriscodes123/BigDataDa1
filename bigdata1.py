# Given Dataset
dataset = """
1,Chair,Furniture
2,Table,Furniture
3,Laptop,Electronics
4,Phone,Electronics
5,Book,Books
6,Desk,Furniture
7,TV,Electronics
8,Novel,Books
9,Monitor,Electronics
10,Sofa,Furniture
11,Armchair,Furniture
12,Smartwatch,Electronics
13,Bookshelf,Furniture
14,Camera,Electronics
15,E-reader,Books
16,Recliner,Furniture
17,Tablet,Electronics
18,Magazine,Books
19,Console,Furniture
20,Headphones,Electronics
21,Painting,Furniture
22,Router,Electronics
23,Dictionary,Books
24,Desk Lamp,Furniture
25,Speaker,Electronics
26,Calendar,Books
27,Barstool,Furniture
28,Projector,Electronics
29,Journal,Books
30,Workstation,Furniture
31,Microwave,Electronics
32,Atlas,Books
33,Bookshelf,Furniture
34,Television,Electronics
35,Notebook,Books
36,Coffee Table,Furniture
37,TV Stand,Furniture
38,Printer,Electronics
39,Reference Book,Books
40,Bean Bag,Furniture
41,Subwoofer,Electronics
42,Graphic Novel,Books
43,Storage Cabinet,Furniture
44,Blender,Electronics
45,Encyclopedia,Books
46,Armchair,Furniture
47,Smart TV,Electronics
48,Comic Book,Books
49,Side Table,Furniture
50,Electric Fan,Electronics
51,Travel Book,Books
52,Entertainment Unit,Furniture
53,Projector Screen,Electronics
54,Recipe Book,Books
55,Swivel Chair,Furniture
56,Video Camera,Electronics
57,Bookcase,Books
58,Bookend,Furniture
59,Satellite Dish,Electronics
60,Textbook,Books
61,Corner Shelf,Furniture
62,Sound Bar,Electronics
63,Children's Book,Books
64,Wooden Chair,Furniture
65,Home Theater,Electronics
66,Guidebook,Books
67,Storage Bench,Furniture
68,Camera Lens,Electronics
69,Poetry Book,Books
70,File Cabinet,Furniture
71,Digital Camera,Electronics
72,Science Fiction Book,Books
73,End Table,Furniture
74,Home Assistant,Electronics
75,Historical Book,Books
76,Footstool,Furniture
77,Smart Speaker,Electronics
78,Travel Guide,Books
79,Lamp,Furniture
80,Smartphone,Electronics
81,Adventure Book,Books
82,Hallway Table,Furniture
83,Headset,Electronics
84,Novel Collection,Books
85,Outdoor Chair,Furniture
86,TV Mount,Electronics
87,Book Organizer,Books
88,Wall Unit,Furniture
89,Digital Frame,Electronics
90,Instruction Manual,Books
91,Dining Chair,Furniture
92,DVD Player,Electronics
93,Science Book,Books
94,Sofa Bed,Furniture
95,Portable Speaker,Electronics
96,Recipe Collection,Books
97,Computer Desk,Furniture
98,Action Camera,Electronics
99,Comic Collection,Books
100,Armchair,Furniture
101,Sound System,Electronics
102,Library Book,Books
103,Accent Chair,Furniture
104,Smart Light,Electronics
105,Art Book,Books
106,End Table,Furniture
107,Digital Assistant,Electronics
108,Reference Guide,Books
109,Reading Chair,Furniture
110,Media Center,Electronics
111,Travelogue,Books
112,Bean Bag Chair,Furniture
113,Power Bank,Electronics
114,Classics Book,Books
115,Wooden Table,Furniture
116,HDTV,Electronics
117,Children's Encyclopedia,Books
118,Reclining Chair,Furniture
119,Home Theater System,Electronics
120,Autobiography,Books
121,Floor Lamp,Furniture
122,Surround Sound System,Electronics
123,Travel Book Collection,Books
124,Console Table,Furniture
125,Smart Hub,Electronics
126,Dictionary Collection,Books
127,Office Chair,Furniture
128,Smartphone Stand,Electronics
129,Book Collection,Books
130,Kitchen Table,Furniture
131,Game Console,Electronics
132,Magazine Collection,Books
133,Armchair,Furniture
134,Smart TV Stand,Electronics
135,Novel Set,Books
136,Side Chair,Furniture
137,Home Security Camera,Electronics
138,Textbook Collection,Books
139,Patio Furniture,Furniture
140,Streaming Device,Electronics
141,Book Shelf,Books
142,Desk Chair,Furniture
143,Virtual Reality Headset,Electronics
144,Book Collection,Books
145,Storage Shelf,Furniture
146,Electric Kettle,Electronics
147,Study Guide,Books
148,Desk Organizer,Furniture
149,Headphone Stand,Electronics
150,Cookbook,Books
151,Wall Shelf,Furniture
152,Digital Recorder,Electronics
153,Illustrated Book,Books
154,Office Desk,Furniture
155,Home Audio System,Electronics
156,Classic Collection,Books
157,Decorative Chair,Furniture
158,Tablet Stand,Electronics
159,Travel Diary,Books
160,Reading Lamp,Furniture
161,Audio Mixer,Electronics
162,Educational Book,Books
163,Chaise Lounge,Furniture
164,Home Theater Projector,Electronics
165,Photo Album,Books
166,Book Cabinet,Furniture
167,LED TV,Electronics
168,Reading Collection,Books
169,Living Room Chair,Furniture
170,Electric Stove,Electronics
171,Encyclopedic Dictionary,Books
172,Armchair,Furniture
173,Smart Projector,Electronics
174,Travel Journal,Books
175,Bean Bag Chair,Furniture
176,Home Entertainment System,Electronics
177,Picture Book,Books
178,Outdoor Furniture,Furniture
179,Smartwatch Charger,Electronics
180,Book of Poems,Books
181,Desk Lamp,Furniture
182,Wireless Speaker,Electronics
183,Educational Guide,Books
184,Office Furniture,Furniture
185,Digital Assistant Device,Electronics
186,Children's Storybook,Books
187,Reading Chair,Furniture
188,Portable Projector,Electronics
189,Science Collection,Books
190,Wooden Desk,Furniture
191,Home Automation System,Electronics
192,Adventure Collection,Books
193,Decorative Table,Furniture
194,Smart Home Device,Electronics
195,Classic Literature,Books
196,End Table,Furniture
197,Digital Camera Lens,Electronics
198,Travel Guidebook,Books
199,Reclining Sofa,Furniture
200,Smart TV Remote,Electronics
"""

# Convert the dataset string into a list of lines
data = dataset.strip().split('\n')

# Map Phase
def map_function(data):
    mapped = []
    for line in data:
        item_id, item_name, category = line.split(',')
        mapped.append((category, 1))
    return mapped

# Reduce Phase
def reduce_function(mapped_data):
    reduced = {}
    for key, value in mapped_data:
        if key in reduced:
            reduced[key] += value
        else:
            reduced[key] = value
    return reduced

# Execute MapReduce
mapped_data = map_function(data)
reduced_data = reduce_function(mapped_data)

# Display Results
print("Category counts:")
for category, count in reduced_data.items():
    print(f"Category: {category}, Count: {count}")
Дадено е податочно множество во променливата dataset. Последната колона ја претставува класата (0 или 1). Сите атрибути кои ги содржи се од нумерички тип.

Потребно е да направите 4 модели на класификација:

Наивен баесов класификатор.
Дрво на одлука со ентропија како критериум за избор на најдобар атрибут за поделба.
Класификатор со колекција од 4 дрва на одлука со ентропија како критериум за избор на најдобар атрибут за поделба.
Невронска мрежа со 10 неврони, ReLU активациска функција, 0.001 рата на учење.
Од стандарден влез се чита процентот на примероци за поделба. Првите X% од секоја класа се земаат за тренирање, додека останатите примероци се за тестирање. 

Изградете ги моделите на класификација и одредете кој од нив има најголема точност. На стандарден излез испечатете кој е класификаторот со најголема точност. (Najgolema tocnost ima klasifikatorot Naive Bayes/Decision Tree/Random Forest/MLP)

Потоа изградете уште еден модел за класификација со колекција на класификатори на следниот начин:

Класификаторот кој има најголема точност има тежина на глас 2 (класата која ја предвидува класификаторот со најголема точност добива 2 гласа)
Сите останати класификатори имаат тежина на глас 1
За предвидена се смета класата која што ќе добие најголем број гласови
На пример, ако класификаторот со најголема точност и уште еден класификатор ја предвидат класата 0, а останатите два класификатори ја предвидат класата 1, тогаш класата 0 ќе има 3 гласа, а класата 1 ќе има 2 гласа. Класификаторот ја предвидува класата 0.
Пресметајте и испечатете го одзивот на овој модел (колекцијата од класификатори).

одзив = TP / (TP + FN)

TP - број на точно предвидени позитивни класи

FP - број на грешно предвидени позитивни класи

TN - број на точно предвидени негативни класи

FN - број на грешно предвидени негативни класи
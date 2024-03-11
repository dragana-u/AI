Овој проблем се базира на играта Minesweeper.

Креирајте функција која како влез зема листа од # и -, каде што секој хаш знак (#) претставува мина, а секоја цртичка (-) претставува поле без мина. Функцијата треба да враќа листа каде што секоја цртичка е заменета со бројка која го претставува бројот на мини од најблиските полиња на моменталното поле (хоризонтално, вертикално, и дијагонално). Листата која се враќа на излез креирајте ја со пристапот list comprehension.

Од стандарден влез е дадена големината на полето N (полето е со димензии NxN), како и репрезентацијата на полето со # и -. Потребно е да направите репрезентација на полето преку листа од листи, каде што елементите се # и -. Оваа листа е влез на претходно дефинираната функција, а излезот од функцијата е потребно да се испечати од стандарден влез.

Помош: влезот е зададен ред по ред за секоја редица во полето, додека индивидуалните елементи се одвоени со 3 празни места. За да се одделат елементите со 3 празни места, може да ја искористите функцијата split() дефинирана на стрингови. За печатење на излезот може да ја користите функцијата join() дефинирана на стрингови.
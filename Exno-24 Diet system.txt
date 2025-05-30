diet_plan(heart_disease, 'Avoid saturated fats and high sodium foods. Eat more fruits, vegetables, and whole grains.').

diet_plan(diabetes, 'Limit carbohydrates and sugar intake. Focus on lean proteins, non-starchy vegetables, and whole grains.').

diet_plan(hypertension, 'Reduce salt intake. Consume low-fat dairy, lean proteins, and plenty of fruits and vegetables.').

suggest_diet(Disease) :-
    diet_plan(Disease, Plan),
    write('For '), write(Disease), write(':'), nl,
    write(Plan), nl.

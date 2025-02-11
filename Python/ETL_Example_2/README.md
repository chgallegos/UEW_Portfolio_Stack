# SCHOOL DISTRICT ANALYSIS
----
## Overview

The purpose of this school district analysis was to conduct an analysis that excluded Thomas High School 9th grade's scores for both Math and Reading. The background given on the why of this decision was because the school board states that the data used shows evidence of academic dishonesty; specifically, reading and math grades for Thomas High School ninth graders, which appear to have been altered. 

----
## Results

How is the district summary affected?
In the initial analysis, the district summary showed a slightly higher Average Math Score as well as a higher % of Passing Reading, this also influenced a change that can be seen on the % Overall Passing that reduced from a 65.2% to a 64.9%. The reason that the change are not substancial is because the numbers calculated in the new summary are based on the new_student_count, which excluded the students with NaN values.

#### New_total_student_count

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/new_total_student_count.png)

#### District Summary Including 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/district_summary_module.png)

#### District Summary Excluding 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/district_summary_challenge.png)

### How is the school summary affected?

We can see in the school summary that removing the 9th grade data affects the school summary in a more substantial way for the **"Passing Math"**, **"Passing Reading"** and **"Overall Passing"** percentages.

#### School Summary Including 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/school_summary_module.png)

#### School Summary Excluding 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/school_summary_challenge.png)

How does replacing the ninth graders’ math and reading scores affect Thomas High School’s performance relative to the other schools?

The performance relative to other school's was not substantially affected because the removal of 9th grade data also was taken into consideration on the denominator for the calculation of the percentages. Basically, the performance for Thomas High School was calculated only considering 10th to 12th grade data.

#### School Summary calculated from 10th - 12th grade data

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/school_summary_excluding_9th_%20grade.png)

#### Performance Including 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/top_five_module.png)

#### Performance calculated from 10th - 12th grade data

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/top_five_challenge.png)

How does replacing the ninth-grade scores affect the following:
-**Math and reading scores by grade** were unnafected other than the fact that the data showing was NaN 

#### Math scores by grade including 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/math_scores_by_grade_module.png)

#### Reading scores by grade including 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/reading_scores_by_grade_module.png)

#### Math scores by grade excluding 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/math_scores_by_grade_challenge.png)

#### Reading scores by grade excluding 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/reading_scores_by_grade_challenge.png)

-**Scores by school spending**  was affected in the range of $631-$645 as this is the category for average spent per student that Thomas High School falls under

#### Per school spending including 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/per_school_spending_module.png)

#### Per school spending excluding 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/per_school_spending_challenge.png)

-**Scores by school size** were affected but not in a very significant way as the difference in overall passing percentage was approximately 0.3%

#### Per school spending including 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/per_school_size_module.png)

#### Per school spending excluding 9th grade

![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/per_school_size_challenge.png)

-**Scores by school type** only seemed to affect charter type schools by a small percentage from 90.43% to 90.39%

#### Per school spending including 9th grade


FIX URL
![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/per_school_type_module.png)

#### Per school spending excluding 9th grade

FIX URL
![Screenshot](https://github.com/chgallegos/school_district_analysis/blob/main/Resources/per_school_type_challenge.png)
----
## Summary 

In summary, after the ninth grade reading and math scores were replaced with Nans, we have been able to conclude that the major effect that was had was in the school summary calculated before considering the analysis only the 10th to 12th grade data. The analysis also changed numbers in the **scores by school spending** segment for the range of $631-$645. Another category that was influenced by this was -**Scores by school type** in which only charter schools number were affected. Lastly, the **Scores by school size** were affected but not in a significant way.

# Database Design for Cell Count Data Analysis

## 1. Database Schema

**Tables:**

1. **Projects**
   - project_id (Primary Key)
   - project_name
   - description

2. **Patients**
   - patient_id (Primary Key)
   - sex (Male/Female)
   - condition (e.g., melanoma)
   - treatment (e.g., tr1)
   - response (y/n)

3. **Samples**
   - sample_id (Primary Key)
   - patient_id (Foreign Key)
   - project_id (Foreign Key)
   - sample_type (e.g., PBMC)
   - time_from_treatment_start (baseline = 0, e.g., 0, 1, 2...)

4. **Cell Counts**
   - cell_count_id (Primary Key)
   - sample_id (Foreign Key)
   - population (e.g., b_cell, cd8_t_cell)
   - count
   - percentage

## 2. Advantages of Using a Database

- **Scalability**: Can handle thousands of samples efficiently.
- **Data Integrity**: Enforces relationships between projects, patients, and samples.
- **Query Flexibility**: Enables complex analytics, such as responder vs. non-responder comparisons.
- **Efficient Storage**: Avoids data redundancy by normalizing tables.
- **Security & Access Control**: Can implement permissions for different users.


## 3. Query: Number of Subjects per Condition

```sql
SELECT condition, COUNT(DISTINCT patient_id) AS num_subjects
FROM patients
GROUP BY condition;
```

## 4. Query: Retrieve Melanoma PBMC Samples at Baseline for Patients with Treatment tr1

```sql
SELECT s.sample_id, s.patient_id, s.time_from_treatment_start, p.response
FROM samples s
JOIN patients p ON s.patient_id = p.patient_id
WHERE p.condition = 'melanoma'
AND s.sample_type = 'PBMC'
AND s.time_from_treatment_start = 0
AND p.treatment = 'tr1';
```

## 5. Queries for Breakdown of Samples in (4)

### a. Number of Samples per Project

```sql
SELECT s.project_id, COUNT(s.sample_id) AS num_samples
FROM samples s
JOIN patients p ON s.patient_id = p.patient_id
WHERE p.condition = 'melanoma'
AND s.sample_type = 'PBMC'
AND s.time_from_treatment_start = 0
AND p.treatment = 'tr1'
GROUP BY s.project_id;
```

### b. Number of Responders vs. Non-Responders

```sql
SELECT p.response, COUNT(s.sample_id) AS num_samples
FROM samples s
JOIN patients p ON s.patient_id = p.patient_id
WHERE p.condition = 'melanoma'
AND s.sample_type = 'PBMC'
AND s.time_from_treatment_start = 0
AND p.treatment = 'tr1'
GROUP BY p.response;
```

### c. Number of Males and Females

```sql
SELECT p.sex, COUNT(s.sample_id) AS num_samples
FROM samples s
JOIN patients p ON s.patient_id = p.patient_id
WHERE p.condition = 'melanoma'
AND s.sample_type = 'PBMC'
AND s.time_from_treatment_start = 0
AND p.treatment = 'tr1'
GROUP BY p.sex;
```
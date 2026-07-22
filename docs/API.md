# API Documentation

## Base URL

```
http://127.0.0.1:8000
```

---

## Authentication

### Signup

POST

```
/auth/signup
```

### Login

POST

```
/auth/login
```

### Profile

GET

```
/auth/profile
```

Requires JWT Token.

---

## Calculator

POST

```
/calculator/calculate
```

Supported Operations

- add
- sub
- mul
- div
- mod
- power
- sqrt
- percent

---

## History

### Get History

GET

```
/history
```

Supports

- Search
- Pagination

### Delete History

DELETE

```
/history/{id}
```

---

## Statistics

GET

```
/statistics
```

Returns

- Total Calculations
- Average Result
- Today's Calculations
- Most Used Operation

---

## Export

GET

```
/export
```

Downloads CSV file.

---

## Health Check

GET

```
/health
```

Returns API status.
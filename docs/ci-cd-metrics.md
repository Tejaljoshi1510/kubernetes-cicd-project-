# CI/CD Metrics

## Metrics tracked

### 1. Build duration
Measure the time from the start of the GitHub Actions job
until the job finishes.

Source: GitHub Actions workflow run duration.

### 2. Test pass/fail rate
Track the number of passed and failed tests in each workflow run.

Pass rate (%) = Passed tests / Total tests * 100

### 3. Code coverage
Measure the percentage of application code executed by tests.

Minimum required coverage: 80%.

The CI pipeline fails if coverage falls below this threshold.

## Recording results

For each workflow run, record:

| Date | Branch | Duration | Passed | Failed | Coverage | Result |
|------|--------|----------|--------|--------|----------|--------|
| Fill after first run | feature/ci-cd-pipeline | Actual duration | Actual count | Actual count | Actual % | Pass/Fail |

Use actual values from GitHub Actions rather than estimated values.

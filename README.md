
## Automated Kubernetes Demo

Run the complete end-to-end demo with one command:

```bash
chmod +x scripts/demo.sh
./scripts/demo.sh
```

The script:
- Deploys Nginx and PostgreSQL.
- Displays service ports.
- Creates a PostgreSQL table and inserts test data.
- Verifies database records.
- Checks persistent volume claims.
- Recreates the PostgreSQL pod and verifies data persistence.
- Displays the Nginx access URL.

### Access the application

Open the Nginx URL printed by the script.

### Expected verification

- Nginx deployment rolls out successfully.
- PostgreSQL pod reaches Ready status.
- PostgreSQL query returns the test record.
- PVC remains Bound.
- The test record remains after PostgreSQL pod recreation.

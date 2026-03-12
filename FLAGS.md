⚙️ CPU AI Lab CLI Flags Reference

CPU AI Lab’s ./lab script supports several command-line options to customize how the environment starts. This file explains each flag and gives usage examples.

1️⃣ ``--no-logs``

**Description:**
Disables real-time streaming of container logs during startup. Useful for:

* Cleaner output in scripts or CI/CD pipelines
* Faster startup when you don’t need to watch logs

**Usage:**

```bash
# Start CPU AI Lab without streaming logs
./lab up --no-logs
```

**Notes:**

* Containers still start normally
* Health checks still run unless combined with ``--fast-start``


2️⃣ ``--fast-start``

**Description:**
Skips health checks for all services. Useful when you want to:

* Start containers quickly
* Avoid waiting for endpoints to respond during testing

**Usage:**

```bash
# Start CPU AI Lab quickly without waiting for service readiness
./lab up --fast-start
```

**Notes:**

* Containers will be running but some services may not be fully ready yet
* Combine with ``--no-logs`` for a completely silent, fast startup


3️⃣ **Combined Flags**

You can combine flags for a fast, clean startup:

```bash
# Fastest startup: skip health checks and logs
./lab up --no-logs --fast-start
```

**Behavior:**

* Removes old containers, volumes, and network
* Builds/pulls images and starts all containers
* Skips logs and health checks
* Suitable for automated scripts or quick resets


4️⃣ **Recommended Usage**

*New installs / full setup:*

```bash
./lab up
```

*Automated scripts / CI/CD:*

```bash
./lab up --no-logs
```

*Quick testing / dev environment:*

```bash
./lab up --no-logs --fast-start
```

✅ Tip: Flags are optional — running ./lab up without any flags gives a full startup with logs and health checks.



# 🌐 Supabase Connectivity Guide: Fixing DNS & IPv6 Errors

If you are seeing "could not translate host name" or "Network is unreachable", it is because your current network (or your ISP) does not fully support **IPv6**, which is what Supabase uses for direct database connections.

### 🚀 Solution 1: Use the Transaction Pooler (Recommended)
Supabase provides a "Pooler" URL that works on **IPv4** (standard internet).

1.  Go to your **Supabase Dashboard**.
2.  Go to **Project Settings** -> **Database**.
3.  Scroll down to **Connection Pooler**.
4.  Enable the Pooler (if not already enabled).
5.  Copy the **Connection String** using the **Transaction** mode.
6.  It should look like this: `postgresql://postgres.[PROJ_ID]:[PASSWORD]@aws-0-[REGION].pooler.supabase.com:6543/postgres`
7.  Update your `DB_URL` in `db_setup.py` and `real_time_dashboard.py` with this new string.

### 🛠️ Solution 2: Use the IPv6 Direct address
I have already implemented a fallback in the code using `[2406:da14:271:9921:64a7:b634:3a27:1c5c]`. If this still fails with "Network is unreachable", it means your router/net cannot route to IPv6 addresses. Please use **Solution 1** above.

---
### 🧪 Why does this happen?
Modern cloud services (like Supabase on AWS) are moving to IPv6-only for database endpoints to save address space. If you are on an older office/home network, you might need the "Pooler" to bridge the connection.

**Your credentials are correct. Your code is correct. This is purely a network-bridge requirement.**

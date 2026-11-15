---
id: learning.zephyr-docs.bluetooth.page-74
title: Mesh配置数据库
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/cdb_usage.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="configuration-database-cdb"></a>

<a id="bluetooth-mesh-cdb-usage"></a>

# 第74章\_配置数据库（Configuration Database，CDB）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/cdb_usage.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：CDB 是配网器对网络的本地管理记录。正文中的“专有设计”指这一数据库设计不是 Bluetooth SIG 定义的标准数据格式，不是在说明源码许可证。单个 CDB 的存储、配网器本机密钥同步以及多配网器之间的同步是不同问题；最后一种没有内置协调机制。

<a id="contents"></a>

- <a id="id1"></a>

  [概述（Overview）](#overview)

  - <a id="id2"></a>

    [主要功能（Key features）](#key-features)

- <a id="id3"></a>

  [配置选项（Configuration options）](#configuration-options)

- <a id="id4"></a>

  [数据结构（Data Structures）](#data-structures)

  - <a id="id5"></a>

    [节点结构（Node structure）](#node-structure)

  - <a id="id6"></a>

    [子网结构（Subnet structure）](#subnet-structure)

  - <a id="id7"></a>

    [应用密钥结构（Application Key structure）](#application-key-structure)

  - <a id="id8"></a>

    [CDB 主结构（Main CDB structure）](#main-cdb-structure)

- <a id="id9"></a>

  [使用场景（Usage scenarios）](#usage-scenarios)

  - <a id="id10"></a>

    [配网器初始化（Provisioner initialization）](#provisioner-initialization)

  - <a id="id11"></a>

    [配网与节点分配（Provisioning and node allocation）](#provisioning-and-node-allocation)

  - <a id="id12"></a>

    [子网与密钥管理（Subnet and key management）](#subnet-and-key-management)

  - <a id="id13"></a>

    [子网查找与移除（Subnet lookup and removal）](#subnet-lookup-and-removal)

  - <a id="id14"></a>

    [设置应用密钥（Setting up application keys）](#setting-up-application-keys)

  - <a id="id15"></a>

    [应用密钥查找与移除（Application keys lookup and removal）](#application-keys-lookup-and-removal)

  - <a id="id16"></a>

    [节点配置（Node configuration）](#node-configuration)

  - <a id="id17"></a>

    [遍历节点（Iterating over nodes）](#iterating-over-nodes)

  - <a id="id18"></a>

    [节点查找与移除（Node lookup and removal）](#node-lookup-and-removal)

  - <a id="id19"></a>

    [IV 索引管理（IV Index management）](#iv-index-management)

  - <a id="id20"></a>

    [使用设备密钥（Working with device keys）](#working-with-device-keys)

  - <a id="id21"></a>

    [清空 CDB（Clearing the CDB）](#clearing-the-cdb)

- <a id="id22"></a>

  [最佳实践（Best practices）](#best-practices)

- <a id="id23"></a>

  [常见问题（Common pitfalls）](#common-pitfalls)

- <a id="id24"></a>

  [API 参考（API reference）](#api-reference)

- <a id="id25"></a>

  [相关文档（Related documentation）](#related-documentation)

<a id="overview"></a>

## 74.1 [概述（Overview）](#id1)

配置数据库（Configuration Database，CDB）是面向 Bluetooth Mesh 配网器设备的子系统。它保存并管理网络信息，包括已配网节点、网络密钥和应用密钥，使配网器能够跟踪网络拓扑、分配地址并系统地配置节点。

注意（Note）

CDB 的实现采用专有设计，并不遵循 Bluetooth SIG 规范。

通过 [`CONFIG_BT_MESH_CDB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CDB) 启用 CDB，通常只在网络的配网器设备上使用。为避免冲突，Mesh 网络中应只有一台设备启用 CDB。

<a id="key-features"></a>

### 74.1.1 [主要功能（Key features）](#id2)

- 持久化存储（Persistent Storage）：启用 [`CONFIG_BT_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS) 后，可持久化保存全部 CDB 数据，使配网器重启后恢复网络状态。

- 地址管理（Address Management）：自动分配和跟踪已配网节点的单播地址。

- 密钥管理（Key Management）：保存并同步网络密钥和应用密钥。

- 节点跟踪（Node Tracking）：维护各已配网节点的 UUID、地址、元素数量、设备密钥和配置状态。

- IV 索引管理（IV Index Management）：跟踪网络的 IV 索引和 IV 更新状态。

<a id="configuration-options"></a>

## 74.2 [配置选项（Configuration options）](#id3)

以下 Kconfig 选项控制 CDB 容量：

- [`CONFIG_BT_MESH_CDB_NODE_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CDB_NODE_COUNT)：CDB 可处理的最大节点数。

- [`CONFIG_BT_MESH_CDB_SUBNET_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CDB_SUBNET_COUNT)：CDB 可处理的最大子网数。

- [`CONFIG_BT_MESH_CDB_APP_KEY_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CDB_APP_KEY_COUNT)：CDB 可处理的最大应用密钥数。

其他选项：

- [`CONFIG_BT_MESH_CDB_KEY_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CDB_KEY_SYNC)：启用配网器节点的 Mesh 密钥与 CDB 密钥之间的自动同步。启用后，通过配置服务端执行的密钥操作会自动同步到 CDB。 相关链接：[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

<a id="data-structures"></a>

## 74.3 [数据结构（Data Structures）](#id4)

CDB 用多个数据结构组织收集的数据，分别表示节点、子网、应用密钥和整个数据库状态。

<a id="node-structure"></a>

### 74.3.1 [节点结构（Node structure）](#id5)

```c
struct bt_mesh_cdb_node {
	/** Node UUID */
	uint8_t  uuid[16];
	/** Primary element address */
	uint16_t addr;
	/** Network key index used during provisioning */
	uint16_t net_idx;
	/** Number of elements */
	uint8_t  num_elem;
	/** Device key */
	struct bt_mesh_key dev_key;
	/** Node flags */
	ATOMIC_DEFINE(flags, BT_MESH_CDB_NODE_FLAG_COUNT);
};
```

> 译注——代码说明：节点结构：`uuid` 为节点 UUID；`addr` 为主元素地址；`net_idx` 为配网所用网络密钥索引；`num_elem` 为元素数量；`dev_key` 为设备密钥容器；`flags` 为原子节点标志。结构原定义来自 `include/zephyr/bluetooth/mesh/cdb.h`，不要把它复制到应用重新定义。

节点标志：

- `BT_MESH_CDB_NODE_CONFIGURED`：节点已配置密钥和绑定关系后设置。

<a id="subnet-structure"></a>

### 74.3.2 [子网结构（Subnet structure）](#id6)

```c
struct bt_mesh_cdb_subnet {
	/** Network key index */
	uint16_t net_idx;
	/** Key Refresh phase */
	uint8_t kr_phase;
	/** Old and new keys for Key Refresh */
	struct {
		struct bt_mesh_key net_key;
	} keys[2];
};
```

> 译注——代码说明：子网结构：`net_idx` 为网络密钥索引，`kr_phase` 为密钥刷新阶段（Key Refresh phase），`keys[2]` 保存刷新流程中的旧、新网络密钥。数组位置不是网络密钥索引。

<a id="application-key-structure"></a>

### 74.3.3 [应用密钥结构（Application Key structure）](#id7)

```c
struct bt_mesh_cdb_app_key {
	/** Bound network key index */
	uint16_t net_idx;
	/** Application key index */
	uint16_t app_idx;
	/** Old and new keys for Key Refresh */
	struct {
		struct bt_mesh_key app_key;
	} keys[2];
};
```

> 译注——代码说明：应用密钥结构：`net_idx` 指绑定的网络密钥索引，`app_idx` 指应用密钥索引；`keys[2]` 保存密钥刷新中的旧、新应用密钥。

<a id="main-cdb-structure"></a>

### 74.3.4 [CDB 主结构（Main CDB structure）](#id8)

```c
struct bt_mesh_cdb {
	/** Network IV Index */
	uint32_t iv_index;
	/** Lowest available unicast address for provisioning */
	uint16_t lowest_avail_addr;
	/** Flags for CDB state (private) */
	ATOMIC_DEFINE(flags, BT_MESH_CDB_FLAG_COUNT);
	/** Nodes in the mesh network */
	struct bt_mesh_cdb_node nodes[NODE_COUNT];
	/** Subnets in the mesh network */
	struct bt_mesh_cdb_subnet subnets[SUBNET_COUNT];
	/** Application keys in the mesh network */
	struct bt_mesh_cdb_app_key app_keys[APP_KEY_COUNT];
};

/** The global CDB instance is accessible through this variable. */
extern struct bt_mesh_cdb bt_mesh_cdb;
```

> 译注——代码说明：主结构：`iv_index` 是网络 IV 索引；`lowest_avail_addr` 是配网可用的最低单播地址；`flags` 为内部状态标志；`nodes`、`subnets`、`app_keys` 分别保存节点、子网和应用密钥。全局实例通过变量 `bt_mesh_cdb` 访问，数组容量由配置决定。

<a id="usage-scenarios"></a>

## 74.4 [使用场景（Usage scenarios）](#id9)

以下模式演示常见的 CDB 使用场景：

- 配网器初始化：创建和初始化 CDB。 相关链接：[配网器初始化（Provisioner initialization）](#cdb-pattern-1)。

- 配网与节点分配：管理节点配网和地址。 相关链接：[配网与节点分配（Provisioning and node allocation）](#cdb-pattern-2)。

- 子网与密钥管理：管理网络密钥和子网。 相关链接：[子网与密钥管理（Subnet and key management）](#cdb-pattern-3)。

- 子网查找与移除：查找、移除子网。 相关链接：[子网查找与移除（Subnet lookup and removal）](#cdb-pattern-4)。

- 设置应用密钥：向 CDB 添加应用密钥。 相关链接：[设置应用密钥（Setting up application keys）](#cdb-pattern-5)。

- 应用密钥查找与移除：查找、移除应用密钥。 相关链接：[应用密钥查找与移除（Application keys lookup and removal）](#cdb-pattern-6)。

- 节点配置：配置已配网节点。 相关链接：[节点配置（Node configuration）](#cdb-pattern-7)。

- 遍历节点：通过回调处理节点。 相关链接：[遍历节点（Iterating over nodes）](#cdb-pattern-8)。

- 节点查找与移除：查找、移除节点。 相关链接：[节点查找与移除（Node lookup and removal）](#cdb-pattern-9)。

- IV 索引管理：管理 IV 索引更新。 相关链接：[IV 索引管理（IV Index management）](#cdb-pattern-10)。

- 使用设备密钥：导入、导出设备密钥。 相关链接：[使用设备密钥（Working with device keys）](#cdb-pattern-11)。

- 清空 CDB：重置数据库。 相关链接：[清空 CDB（Clearing the CDB）](#cdb-pattern-12)。

注意（Note）

以下场景代码应作为概念模式理解，不是可直接使用的完整实现。必须按应用上下文调整并测试；正确用法请阅读 CDB API 说明。

<a id="provisioner-initialization"></a>

<a id="cdb-pattern-1"></a>

### 74.4.1 [配网器初始化（Provisioner initialization）](#id10)

在嵌入式配网器节点上，必须先初始化 CDB，再完成本机 Mesh 协议栈的配网，之后应用才能用它保存密钥、跟踪节点并进行配置。此步骤建立主网络密钥、初始子网、起始 IV 索引和地址空间，使后续 CDB 操作具有明确的网络上下文，并能跨重启持久保存。

典型配网器在启动期间初始化 CDB：

```c
#include <zephyr/bluetooth/mesh.h>

static int provisioner_init(void)
{
    uint8_t net_key[16];
    int err;

    /* Initialize Bluetooth Mesh */
    err = bt_mesh_init(&prov, &comp);
    if (err) {
        return err;
    }

    /* Load settings if persistent storage is enabled */
    if (IS_ENABLED(CONFIG_BT_SETTINGS)) {
        settings_load();
    }

    /* Generate or use predefined network key */
    bt_rand(net_key, 16);

    /* Create CDB with primary network key */
    err = bt_mesh_cdb_create(net_key);
    if (err == -EALREADY) {
        printk("Using stored CDB\n");
    } else if (err) {
        printk("Failed to create CDB (err %d)\n", err);
        return err;
    } else {
        printk("Created new CDB\n");
    }

    return 0;
}
```

> 译注——代码说明：初始化片段先初始化 Mesh、按配置载入设置，再生成网络密钥并创建 CDB。`Using stored CDB` 表示复用已有记录，`Created new CDB` 表示新建成功，失败打印错误码。`prov`、`comp` 是应用提供的配网回调与组成数据；片段没有给出它们的完整定义，也未完整展示蓝牙初始化、头文件和错误处理。原例未检查 `bt_rand()` 与 `settings_load()` 的返回值，集成时应补齐，不应在失败后继续使用未经确认的密钥或状态。

要点：

- 用主网络密钥调用 [`bt_mesh_cdb_create()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a00490e69b96e88cdf7336ca22e63617d)。

- 若 CDB 已存在，例如已从持久化存储载入，该函数返回错误码。

- 函数自动创建 `NetIdx = 0` 的子网。

- 把 IV 索引设为 `0`，最低可用地址设为 `1`。

<a id="provisioning-and-node-allocation"></a>

<a id="cdb-pattern-2"></a>

### 74.4.2 [配网与节点分配（Provisioning and node allocation）](#id11)

向 Mesh 添加新设备时，其地址、设备密钥和基本元数据必须一致地记录在配网器数据库中。PB-ADV／PB-GATT 配网期间自动分配节点，可使 CDB 与实际网络保持同步；新设备配网时，CDB 自动在配网过程中分配节点。

也可以手工分配节点或检查分配结果。手工分配适用于从外部来源导入节点、预分配地址范围、依据已知信息恢复网络等高级场景。

```c
/* Provisioning callback - node is automatically added to CDB */
static void node_added(uint16_t idx, uint8_t uuid[16], uint16_t addr,
                       uint8_t num_elem)
{
    printk("Node added: addr=0x%04x, elements=%d\n", addr, num_elem);
    /* The CDB node is created automatically by the provisioning subsystem */
}

static const struct bt_mesh_prov prov = {
    .uuid = dev_uuid,
    .node_added = node_added,
    /* ... other callbacks ... */
};

/* Manual node allocation (if needed) */
static struct bt_mesh_cdb_node *allocate_node(const uint8_t uuid[16],
                                                uint8_t num_elem)
{
    struct bt_mesh_cdb_node *node;
    uint16_t addr;

    /* Get free address or specify one (0 = auto-allocate) */
    addr = bt_mesh_cdb_free_addr_get(num_elem);
    if (addr == BT_MESH_ADDR_UNASSIGNED) {
        printk("No free addresses available\n");
        return NULL;
    }

    /* Allocate node in CDB */
    node = bt_mesh_cdb_node_alloc(uuid, addr, num_elem, net_idx);
    if (node == NULL) {
        printk("Failed to allocate node\n");
        return NULL;
    }

    return node;
}
```

> 译注——代码说明：`node_added` 是配网完成添加节点后的回调，CDB 条目由配网子系统自动建立；省略的其他回调仍由应用实现。手工分配分支先按元素数量找空闲地址，再分配条目；无地址或分配失败返回 `NULL`。`dev_uuid` 与 `net_idx` 来自应用上下文，不能直接把该片段当作独立程序。PB-ADV／PB-GATT 分别指广播／GATT 配网承载，其支持范围以所用版本和角色为准。

要点：

- 正常的 PB-ADV／PB-GATT 配网期间，节点自动加入 CDB。

- [`bt_mesh_cdb_node_alloc()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ab0dc86dd674f57a820aa3f5cebf77895) 按指定参数创建 CDB 条目。

- 地址参数传入 [`BT_MESH_ADDR_UNASSIGNED`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga6d11790af686e6d48f08c6f1cd65317c)，可让 CDB 自动分配最低可用地址。

- [`bt_mesh_cdb_free_addr_get()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aa10c4ec973e61626ba6424e443fb0b88) 按给定元素数量查找空闲地址范围。

- 地址分配会检查冲突并确保单播地址有效。

<a id="subnet-and-key-management"></a>

<a id="cdb-pattern-3"></a>

### 74.4.3 [子网与密钥管理（Subnet and key management）](#id12)

大型或分区 Mesh 网络常用多个子网隔离流量域、支持安全迁移或密钥刷新流程。在 CDB 中管理子网及网络密钥，使配网器能够创建子网、轮换密钥，并在配网和配置节点时取得正确标志与 IV 索引。

在 CDB 中管理网络密钥和子网：

```c
/* Add a new subnet */
static int add_subnet(uint16_t net_idx)
{
    struct bt_mesh_cdb_subnet *sub;
    uint8_t net_key[16];
    int err;

    /* Allocate subnet in CDB */
    sub = bt_mesh_cdb_subnet_alloc(net_idx);
    if (sub == NULL) {
        printk("Failed to allocate subnet\n");
        return -ENOMEM;
    }

    /* Generate network key */
    bt_rand(net_key, 16);

    /* Import key value */
    err = bt_mesh_cdb_subnet_key_import(sub, 0, net_key);
    if (err) {
        bt_mesh_cdb_subnet_del(sub, false);
        return err;
    }

    /* Store subnet */
    if (IS_ENABLED(CONFIG_BT_SETTINGS)) {
        bt_mesh_cdb_subnet_store(sub);
    }

    return 0;
}

/* Get subnet for provisioning */
static int get_subnet_flags(uint16_t net_idx)
{
    struct bt_mesh_cdb_subnet *sub;
    uint8_t flags;

    sub = bt_mesh_cdb_subnet_get(net_idx);
    if (sub == NULL) {
        return -ENOENT;
    }

    flags = bt_mesh_cdb_subnet_flags(sub);
    printk("Subnet flags: KR=%d IVU=%d\n",
           !!(flags & BT_MESH_NET_FLAG_KR),
           !!(flags & BT_MESH_NET_FLAG_IVU));

    return 0;
}
```

> 译注——代码说明：新增子网流程为分配条目、生成网络密钥、导入槽位 0、按配置安排保存；导入失败会删除刚分配的条目。查询部分取得子网，再读取配网所需标志，输出 KR（密钥刷新）和 IVU（IV 更新）状态。此操作管理 CDB，本身不会向全部远端节点下发新密钥。

要点：

- [`bt_mesh_cdb_subnet_alloc()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aeba4ed506e30ab8d91746b36e7e5f968) 按 NetIdx 分配子网。

- [`bt_mesh_cdb_subnet_key_import()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aba737b508e0e40dfb5ad9da9d7b6fd11) 设置实际密钥值。

- [`bt_mesh_cdb_subnet_flags()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a121a30fd546ccb887c2c49ceef65c2d6) 返回配网数据所需的标志。

- 标志包含 CDB 中的密钥刷新与 IV 更新状态。

<a id="subnet-lookup-and-removal"></a>

<a id="cdb-pattern-4"></a>

### 74.4.4 [子网查找与移除（Subnet lookup and removal）](#id13)

有时需要检查已有子网，例如用于诊断或工具处理；也可能要彻底移除子网，例如停用网络分区、迁移到新子网或清理实验数据。CDB 提供查找和删除辅助函数，使配网器所记录的活动子网与节点实际使用情况保持一致。

在 CDB 中查找和管理子网：

```c
/* Get subnet by NetIdx */
static void lookup_subnet(uint16_t net_idx)
{
    struct bt_mesh_cdb_subnet *sub;

    sub = bt_mesh_cdb_subnet_get(net_idx);
    if (sub == NULL) {
        printk("Subnet 0x%03x not found\n", net_idx);
        return;
    }

    printk("Subnet 0x%03x: kr_phase=%d\n", net_idx, sub->kr_phase);
}

/* Remove a subnet from the CDB */
static void remove_subnet(uint16_t net_idx)
{
    struct bt_mesh_cdb_subnet *sub;

    sub = bt_mesh_cdb_subnet_get(net_idx);
    if (sub == NULL) {
        printk("Subnet not found\n");
        return;
    }

    /* First, remove the subnet from all nodes in the network */
    /* ... send NetKey Delete to all nodes using Config Client ... */

    /* Delete subnet from CDB */
    bt_mesh_cdb_subnet_del(sub, true);

    printk("Subnet 0x%03x removed\n", net_idx);
}

/* Export subnet key for external use */
static int export_subnet_key(uint16_t net_idx, int key_idx)
{
    struct bt_mesh_cdb_subnet *sub;
    uint8_t net_key[16];
    int err;

    sub = bt_mesh_cdb_subnet_get(net_idx);
    if (sub == NULL) {
        return -ENOENT;
    }

    err = bt_mesh_cdb_subnet_key_export(sub, key_idx, net_key);
    if (err) {
        printk("Failed to export subnet key (err %d)\n", err);
        return err;
    }

    printk("NetKey[%d] for subnet 0x%03x: ", key_idx, net_idx);
    for (int i = 0; i < 16; i++) {
        printk("%02x", net_key[i]);
    }
    printk("\n");

    return 0;
}
```

> 译注——代码说明：查找部分按 NetIdx 获取子网；删除部分的“向所有节点发送 NetKey Delete”仅写在注释中，实际网络操作未实现。导出部分把密钥取到本地缓冲区，随后原例逐字节打印。该打印与本页“生产代码不得暴露密钥”的要求冲突；原例保留供对照，生产实现应去掉密钥输出，导出 API 不会自动阻止调用者泄露明文。

要点：

- [`bt_mesh_cdb_subnet_get()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a34dcf031e675235cdcbe0e1f76c00cf3) 按 NetKeyIndex 获取子网。

- 向 [`bt_mesh_cdb_subnet_del()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a66df2f6b6363af595181fe722122996d) 传入 `true`，可清除持久化存储中的对应数据。

- 从 CDB 删除子网前，务必先从所有节点移除该子网。

- 使用 [`bt_mesh_cdb_subnet_key_export()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ac361a17a704195e852faecda09881203) 安全取得密钥材料。

- `key_idx` 参数（`0` 或 `1`）在密钥刷新过程中选择旧密钥或新密钥。

<a id="setting-up-application-keys"></a>

<a id="cdb-pattern-5"></a>

### 74.4.5 [设置应用密钥（Setting up application keys）](#id14)

应用密钥决定哪些应用流量可加密，以及可绑定到何处。CDB 初始化后，配网器必须创建一个或多个应用密钥，才能绑定节点模型并启用实际应用层通信，例如照明或传感器数据通信。

创建 CDB 后，为节点配置添加应用密钥：

```c
static void setup_cdb_keys(void)
{
    struct bt_mesh_cdb_app_key *key;
    uint8_t app_key[16];
    int err;

    /* Allocate application key in CDB */
    key = bt_mesh_cdb_app_key_alloc(net_idx, app_idx);
    if (key == NULL) {
        printk("Failed to allocate app-key\n");
        return;
    }

    /* Generate random key value */
    bt_rand(app_key, 16);

    /* Import the key into CDB */
    err = bt_mesh_cdb_app_key_import(key, 0, app_key);
    if (err) {
        printk("Failed to import appkey (err %d)\n", err);
        return;
    }

    /* Store to persistent storage */
    if (IS_ENABLED(CONFIG_BT_SETTINGS)) {
        bt_mesh_cdb_app_key_store(key);
    }
}
```

> 译注——代码说明：应用密钥流程为按 `net_idx`、`app_idx` 分配槽位、生成随机值、导入槽位 0，并按配置保存。Failed to allocate／import 分别表示分配或导入失败；原例导入失败后直接返回，集成时还应处理已分配条目的回收及随机数生成失败。

要点：

- [`bt_mesh_cdb_app_key_alloc()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ab82dcdf26d66ea4ab0df34bc23421f39) 在 CDB 中分配一个槽位。

- [`bt_mesh_cdb_app_key_import()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a9ad0651ccaa7ff1f86402ce8c05c9410) 设置实际密钥值。

- 导入函数的第二个参数（`0`）是密钥刷新过程中的密钥索引，`0` 表示当前密钥。

- 使用持久化存储时，创建密钥后务必保存。

<a id="application-keys-lookup-and-removal"></a>

<a id="cdb-pattern-6"></a>

### 74.4.6 [应用密钥查找与移除（Application keys lookup and removal）](#id15)

随着运行推进，可能需要检查应用密钥绑定到哪个网络密钥、轮换或撤销应用密钥，或清理不再使用的密钥。通过 CDB 正确查找和移除，有助于避免悬空绑定，并确保节点与配网器对可用应用密钥具有一致认识。

在 CDB 中查找和管理应用密钥：

```c
/* Get application key by AppIdx */
static void lookup_app_key(uint16_t app_idx)
{
    struct bt_mesh_cdb_app_key *key;

    key = bt_mesh_cdb_app_key_get(app_idx);
    if (key == NULL) {
        printk("AppKey 0x%03x not found\n", app_idx);
        return;
    }

    printk("AppKey 0x%03x: bound to NetIdx 0x%03x\n",
           app_idx, key->net_idx);
}

/* Remove an application key from the CDB */
static void remove_app_key(uint16_t app_idx)
{
    struct bt_mesh_cdb_app_key *key;

    key = bt_mesh_cdb_app_key_get(app_idx);
    if (key == NULL) {
        printk("AppKey not found\n");
        return;
    }

    /* First, remove the app key from all nodes in the network */
    /* ... send AppKey Delete to all nodes using Config Client ... */

    /* Delete app key from CDB */
    bt_mesh_cdb_app_key_del(key, true);

    printk("AppKey 0x%03x removed\n", app_idx);
}

/* Export application key for external use */
static int export_app_key(uint16_t app_idx, int key_idx)
{
    struct bt_mesh_cdb_app_key *key;
    uint8_t app_key[16];
    int err;

    key = bt_mesh_cdb_app_key_get(app_idx);
    if (key == NULL) {
        return -ENOENT;
    }

    err = bt_mesh_cdb_app_key_export(key, key_idx, app_key);
    if (err) {
        printk("Failed to export app key (err %d)\n", err);
        return err;
    }

    printk("AppKey[%d] 0x%03x: ", key_idx, app_idx);
    for (int i = 0; i < 16; i++) {
        printk("%02x", app_key[i]);
    }
    printk("\n");

    return 0;
}

/* Update application key binding */
static int update_app_key_binding(uint16_t app_idx, uint16_t new_net_idx)
{
    struct bt_mesh_cdb_app_key *key;

    key = bt_mesh_cdb_app_key_get(app_idx);
    if (key == NULL) {
        return -ENOENT;
    }

    /* Verify the new subnet exists */
    if (bt_mesh_cdb_subnet_get(new_net_idx) == NULL) {
        printk("Target subnet 0x%03x not found\n", new_net_idx);
        return -ENOENT;
    }

    key->net_idx = new_net_idx;

    /* Store updated binding */
    if (IS_ENABLED(CONFIG_BT_SETTINGS)) {
        bt_mesh_cdb_app_key_store(key);
    }

    printk("AppKey 0x%03x rebound to NetIdx 0x%03x\n",
           app_idx, new_net_idx);

    return 0;
}
```

> 译注——代码说明：本段按 AppIdx 查找、移除和导出应用密钥。向所有节点发送 AppKey Delete 的步骤仍是注释占位；修改 `key->net_idx` 并保存，只改变本地 CDB 绑定，不会自动修改所有节点的密钥状态。导出示例同样打印密钥，生产代码必须去掉该输出。

要点：

- [`bt_mesh_cdb_app_key_get()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ab728a20fdb1535cc7059a39e8490a736) 按 AppKeyIndex 获取应用密钥。

- 向 [`bt_mesh_cdb_app_key_del()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a692c6980c9b0d2da18e8f47d67757f07) 传入 `true`，可清除持久化存储中的对应数据。

- 从 CDB 删除应用密钥前，务必先从所有节点移除该密钥。

- 使用 [`bt_mesh_cdb_app_key_export()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a87cfce7316efabe4c8b24be6c3b6d8b4) 安全取得密钥材料。

- `key_idx` 参数（`0` 或 `1`）在密钥刷新过程中选择旧密钥或新密钥。

- 应用密钥通过 `net_idx` 字段绑定到网络密钥。

<a id="node-configuration"></a>

<a id="cdb-pattern-7"></a>

### 74.4.7 [节点配置（Node configuration）](#id16)

配网只是把节点加入网络，并不会使其自动参与应用。配网后还须添加网络／应用密钥、绑定模型、设置订阅和发布。CDB 保存密钥与配置状态，使配网器重启后能继续配置，并避免重复配置已完成的节点。

配网后，通过添加密钥和绑定模型配置节点：

```c
static void configure_node(struct bt_mesh_cdb_node *node)
{
    NET_BUF_SIMPLE_DEFINE(buf, BT_MESH_RX_SDU_MAX);
    struct bt_mesh_cdb_app_key *key;
    uint8_t app_key[16];
    uint8_t status;
    int err;

    printk("Configuring node 0x%04x\n", node->addr);

    /* Get application key from CDB */
    key = bt_mesh_cdb_app_key_get(app_idx);
    if (key == NULL) {
        printk("App-key not found\n");
        return;
    }

    /* Export key value from CDB */
    err = bt_mesh_cdb_app_key_export(key, 0, app_key);
    if (err) {
        printk("Failed to export key (err %d)\n", err);
        return;
    }

    /* Add application key to the node */
    err = bt_mesh_cfg_cli_app_key_add(net_idx, node->addr,
                                      net_idx, app_idx,
                                      app_key, &status);
    if (err || status) {
        printk("Failed to add app-key (err %d, status %d)\n",
               err, status);
        return;
    }

    /* Get composition data and bind models */
    err = bt_mesh_cfg_cli_comp_data_get(net_idx, node->addr, 0,
                                        &status, &buf);
    if (err || status) {
        printk("Failed to get composition data\n");
        return;
    }

    /* Parse composition and bind models to app key */
    /* ... model binding code ... */

    /* Mark node as configured */
    atomic_set_bit(node->flags, BT_MESH_CDB_NODE_CONFIGURED);

    /* Persist configuration status */
    if (IS_ENABLED(CONFIG_BT_SETTINGS)) {
        bt_mesh_cdb_node_store(node);
    }
}
```

> 译注——代码说明：节点配置流程为从 CDB 取得应用密钥、导出密钥值、发送 AppKey Add、读取组成数据，然后绑定模型并保存配置完成标志。模型解析和绑定仍是注释占位，应补全并确认成功后才能设置标志。另据[官方 cfg_cli.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/mesh/cfg_cli.h)，`bt_mesh_cfg_cli_comp_data_get()` 的 `rsp` 返回的是页号；原例把它存入名为 `status` 的变量并检查非零，不应推广为所有组成数据请求的状态码判断。上一条 AppKey Add 的 `status` 才是该操作的响应状态。

要点：

- 使用 [`bt_mesh_cdb_app_key_get()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ab728a20fdb1535cc7059a39e8490a736) 和 [`bt_mesh_cdb_app_key_export()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a87cfce7316efabe4c8b24be6c3b6d8b4) 获取密钥。

- 用配置客户端模型配置远端节点。

- 配置成功后设置 `BT_MESH_CDB_NODE_CONFIGURED` 标志。

- 务必调用 [`bt_mesh_cdb_node_store()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ac775f3d1be745aeba2979b9ae4b42c4f)，持久化保存已配置状态。

<a id="iterating-over-nodes"></a>

<a id="cdb-pattern-8"></a>

### 74.4.8 [遍历节点（Iterating over nodes）](#id17)

许多管理任务需要处理全部节点或筛选出的节点子集，例如检查哪些节点尚待配置、生成统计或批量操作。CDB 迭代器让配网器能够以安全、抽象的方式遍历全部已知节点，而不依赖内部存储细节。

CDB 提供迭代器来处理所有已分配节点：

```c
/* Check for unconfigured nodes */
static uint8_t check_unconfigured(struct bt_mesh_cdb_node *node,
                                   void *user_data)
{
    if (!atomic_test_bit(node->flags, BT_MESH_CDB_NODE_CONFIGURED)) {
        printk("Node 0x%04x needs configuration\n", node->addr);
        configure_node(node);
    }

    return BT_MESH_CDB_ITER_CONTINUE;
}

static void process_nodes(void)
{
    bt_mesh_cdb_node_foreach(check_unconfigured, NULL);
}

/* Example: Count nodes on a specific subnet */
static uint8_t count_subnet_nodes(struct bt_mesh_cdb_node *node,
                                   void *user_data)
{
    uint16_t *net_idx = user_data;
    static int count = 0;

    if (node->net_idx == *net_idx) {
        count++;
    }

    return BT_MESH_CDB_ITER_CONTINUE;
}
```

> 译注——代码说明：遍历回调检查未配置标志，调用前面的配置函数，并返回继续遍历标志；第二个回调示例按指定子网计数。其 `static int count` 跨回调和多次遍历保留，原片段没有展示清零或读取结果；若要每次重新统计，应在一次遍历开始前初始化由调用方持有的计数上下文。

要点：

- [`bt_mesh_cdb_node_foreach()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ae8ed0ef1a00e973d864c944c9d9400bc) 为每个已分配节点调用回调。

- 返回 `BT_MESH_CDB_ITER_CONTINUE` 继续遍历。

- 返回 `BT_MESH_CDB_ITER_STOP` 提前终止遍历。

- 回调仅针对满足 `addr != BT_MESH_ADDR_UNASSIGNED` 的节点调用。

<a id="node-lookup-and-removal"></a>

<a id="cdb-pattern-9"></a>

### 74.4.9 [节点查找与移除（Node lookup and removal）](#id18)

有时需要检查单个节点，例如调试；也可能要从网络移除节点，例如实际设备退役或被替换。使用 CDB 节点查找和删除操作，可使网络的逻辑记录与实际设备一致，并避免地址重用冲突。

在 CDB 中查找和管理节点：

```c
/* Get node by address */
static void lookup_node(uint16_t addr)
{
    struct bt_mesh_cdb_node *node;

    node = bt_mesh_cdb_node_get(addr);
    if (node == NULL) {
        printk("Node 0x%04x not found\n", addr);
        return;
    }

    printk("Node 0x%04x: %d elements, net_idx=0x%03x\n",
           node->addr, node->num_elem, node->net_idx);
}

/* Remove a node from the network */
static void remove_node(uint16_t addr)
{
    struct bt_mesh_cdb_node *node;

    node = bt_mesh_cdb_node_get(addr);
    if (node == NULL) {
        printk("Node not found\n");
        return;
    }

    /* First, send Node Reset to the device (recommended) */
    /* ... send reset command using Config Client ... */

    /* Delete node from CDB */
    bt_mesh_cdb_node_del(node, true);

    printk("Node 0x%04x removed\n", addr);
}
```

> 译注——代码说明：节点查询按地址查找并打印元素数量与网络索引。移除节点前发送 Node Reset 的步骤仍是注释占位；仅删除 CDB 条目不会实际复位远端设备，应在确认远端处理结果后维护本地记录。

要点：

- [`bt_mesh_cdb_node_get()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a3d0034ec500d3964dd4b428e518abfb9) 按元素地址搜索，节点任一元素的地址都可使用。

- 移除节点前，务必先发送 `Node Reset` 命令，避免留下失去管理的设备。

- 向 [`bt_mesh_cdb_node_del()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a6d9cc2d360075b6b3e939a4979e08895) 传入 `true`，可清除持久化存储中的对应数据。

- 删除节点时，可能在适当条件下更新 `lowest_avail_addr`，详情请阅读 CDB API。

<a id="iv-index-management"></a>

<a id="cdb-pattern-10"></a>

### 74.4.10 [IV 索引管理（IV Index management）](#id19)

IV 索引是 Bluetooth Mesh 安全和重放保护的重要组成部分。发生 IV 更新时，配网器必须更新已保存的 IV 索引，使后续配网和配置使用正确的值与地址空间。把它存入 CDB，可使网络状态在重启前后及各次配网操作之间保持一致。

更新网络的 IV 索引：

```c
/* Update IV Index when IV Update procedure occurs */
static void handle_iv_update(uint32_t iv_index, bool iv_update)
{
    bt_mesh_cdb_iv_update(iv_index, iv_update);

    printk("IV Index updated: %u (IV Update: %s)\n",
           iv_index, iv_update ? "in progress" : "normal");
}

/* The IV Index is automatically used during provisioning */
static void provision_with_current_iv(void)
{
    /* The provisioner automatically uses bt_mesh_cdb.iv_index
     * and bt_mesh_cdb_subnet_flags() when sending provisioning data
     */
}
```

> 译注——代码说明：IV 更新处理调用 `bt_mesh_cdb_iv_update()`；in progress 表示正在更新，normal 表示正常状态。后一个函数只是说明配网器发送配网数据时自动使用 `bt_mesh_cdb.iv_index` 和 `bt_mesh_cdb_subnet_flags()`。原文将最低可用地址重置作概括描述；[官方 cdb.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/cdb.c)实际仅在 `!iv_update` 或新索引超过旧索引加 1 时把 `lowest_avail_addr` 重置为 1。

要点：

- [`bt_mesh_cdb_iv_update()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aa6d124339002c43fc35f301a9eef3e7c) 同时更新 IV 索引和 IV 更新标志。

- CDB 在 IV 索引更新期间自动重置 `lowest_avail_addr`。

- 配网器子系统自动为新节点使用 CDB 的 IV 索引。

<a id="working-with-device-keys"></a>

<a id="cdb-pattern-11"></a>

### 74.4.11 [使用设备密钥（Working with device keys）](#id20)

设备密钥属于敏感信息，通常通过安全密钥存储处理，例如 PSA crypto。CDB 的密钥导入／导出 API 抽象了存储方式，使应用可在配置或外部工具等场景使用设备密钥，而无须破坏安全模型或依赖直接指向密钥存储的指针。

使用密钥管理 API 导入、导出设备密钥：

```c
/* Import a known device key */
static int import_dev_key(struct bt_mesh_cdb_node *node,
                          const uint8_t dev_key[16])
{
    int err;

    err = bt_mesh_cdb_node_key_import(node, dev_key);
    if (err) {
        printk("Failed to import device key (err %d)\n", err);
        return err;
    }

    /* Store updated node */
    if (IS_ENABLED(CONFIG_BT_SETTINGS)) {
        bt_mesh_cdb_node_store(node);
    }

    return 0;
}

/* Export device key for external use */
static int export_dev_key(struct bt_mesh_cdb_node *node)
{
    uint8_t dev_key[16];
    int err;

    err = bt_mesh_cdb_node_key_export(node, dev_key);
    if (err) {
        printk("Failed to export device key (err %d)\n", err);
        return err;
    }

    /* Use the exported key */
    printk("Device key: ");
    for (int i = 0; i < 16; i++) {
        printk("%02x", dev_key[i]);
    }
    printk("\n");

    return 0;
}
```

> 译注——代码说明：设备密钥导入成功后按配置保存节点；导出后得到 16 字节密钥。原例的 Device key 输出会暴露明文，生产代码应移除。`node` 必须指向有效 CDB 节点；导入、导出都应检查返回值，并按应用需要控制导出数据的生命周期。

要点：

- 操作密钥时始终使用导入／导出函数；使用 PSA crypto 时这是必须要求。

- 密钥安全存储，不能通过指针直接访问。

- 配网器在配网过程中自动生成并导入设备密钥。

<a id="clearing-the-cdb"></a>

<a id="cdb-pattern-12"></a>

### 74.4.12 [清空 CDB（Clearing the CDB）](#id21)

恢复出厂设置、测试或建立全新网络时，可能需要清除全部配网与配置数据。清空 CDB 会重置逻辑网络状态，以便从头重建，并避免旧密钥或旧节点条目引起不一致。

重置整个配置数据库：

```c
static void reset_network(void)
{
    printk("Clearing CDB...\n");

    /* Clear all CDB data */
    bt_mesh_cdb_clear();

    printk("CDB cleared\n");
}
```

> 译注——代码说明：清空函数调用 `bt_mesh_cdb_clear()`，Clearing CDB／CDB cleared 分别表示开始和完成本地清理。该函数遍历并移除本机数据库条目，不会通过无线网络自动向每个节点发送复位命令；完整网络退役流程仍须单独处理远端节点。

要点：

- [`bt_mesh_cdb_clear()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a4bf4f49fbd75ee33876ffd34f6c6f76f) 移除全部节点、子网和应用密钥。

- 启用 Kconfig 选项 [`CONFIG_BT_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SETTINGS) 时，还会清除持久化存储中的对应数据。

- 将 CDB 标记为无效；再次使用前必须调用 [`bt_mesh_cdb_create()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#a00490e69b96e88cdf7336ca22e63617d)。

<a id="best-practices"></a>

## 74.5 [最佳实践（Best practices）](#id22)

- 错误处理：检查所有 CDB 函数的返回值，尤其是容量耗尽时可能失败的分配函数。

- 地址管理：除非有特定寻址要求，否则向 [`bt_mesh_cdb_node_alloc()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ab0dc86dd674f57a820aa3f5cebf77895) 传入 `0`，让 CDB 管理地址分配。

- 配置跟踪：配置成功后务必设置 `BT_MESH_CDB_NODE_CONFIGURED` 并保存节点，避免不必要的重复配置。

- 密钥安全：生产代码绝不可记录或暴露密钥；使用导入／导出函数安全处理密钥材料。

- 遍历安全：不要在 [`bt_mesh_cdb_node_foreach()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#ae8ed0ef1a00e973d864c944c9d9400bc) 遍历期间修改 CDB，即添加或移除节点。应先收集地址，再修改。

<a id="common-pitfalls"></a>

## 74.6 [常见问题（Common pitfalls）](#id23)

多个配网器之间的 CDB 同步（CDB synchronization among multiple provisioners）

网络中有多个配网器时，应确保它们同步 CDB，以避免冲突。多个配网器之间须用应用层机制共享 CDB，系统没有内置的 CDB 同步机制。

忘记保存（Forgetting to store）

CDB 修改不会自动持久化。使用持久化存储时，修改后务必调用相应的 `_store()` 函数。

密钥索引错误（Incorrect key index）

导入／导出密钥时，密钥索引参数（`0` 或 `1`）表示密钥刷新数组中的位置，不是 NetIdx 或 AppIdx。

地址冲突（Address conflicts）

手工指定地址时，应确保不与已有节点冲突。使用 [`bt_mesh_cdb_free_addr_get()`](https://docs.zephyrproject.org/latest/doxygen/html/cdb_8h.html#aa10c4ec973e61626ba6424e443fb0b88) 查找可用地址。

容量超限（Over-capacity）

CDB 容量由 Kconfig 固定定义，超过容量会导致分配失败。应监控使用情况，并按需增大容量。

访问无效节点（Accessing invalid nodes）

对 `_get()` 或 `_alloc()` 返回的指针解引用前，务必检查是否为 `NULL`。

<a id="api-reference"></a>

## 74.7 [API 参考（API reference）](#id24)

完整 API 文档见：

- 头文件：[`include/zephyr/bluetooth/mesh/cdb.h`](../../../include/zephyr/bluetooth/mesh/cdb.h)

- 实现：[`subsys/bluetooth/mesh/cdb.c`](../../../subsys/bluetooth/mesh/cdb.c)

<a id="related-documentation"></a>

## 74.8 [相关文档（Related documentation）](#id25)

- [蓝牙 Mesh 配置文件（Bluetooth Mesh Profile）](P024_蓝牙Mesh接口.md#bluetooth-mesh)

- [配网（Provisioning）](P070_Mesh配网.md#bluetooth-mesh-provisioning)

- Mesh Shell 命令：[蓝牙 Mesh Shell（Bluetooth Mesh Shell）](P106_Mesh_Shell.md#bluetooth-mesh-shell)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/cdb_usage.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/cdb_usage.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/cdb_usage.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh运行时配置](P073_Mesh运行时配置.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh统计](P075_Mesh统计.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P073_Mesh运行时配置.md) · [返回大纲](大纲.md) · [下一章](P075_Mesh统计.md)

</details>

<!-- reading-navigation:end -->

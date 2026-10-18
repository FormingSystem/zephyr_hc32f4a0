---
id: learning.zephyr-docs.bluetooth.page-58
title: 协调集标识配置文件CSIP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/csip.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-coordinated-set-identification-profile-shell"></a>

# 第58章\_蓝牙：协调集标识配置文件 Shell（Bluetooth: Coordinated Set Identification Profile Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/audio/csip.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——操作上下文：代码块中的命令在启用了相应音频功能的目标固件 Zephyr Shell 中执行，接入与初始化见[蓝牙 Shell](P007_蓝牙Shell.md)。`uart:~$` 是提示符，后续日志是官方预期输出；不要把提示符、日志或 `<address>` 等占位符原样当作主机终端命令运行。各示例代表不同角色和操作分支，按实际连接与初始化状态选择，不连贯粘贴整章。命令缺失、初始化失败或发现未完成时，应先核对固件配置、控制器能力及当前版本帮助，再继续后续操作。

> 译注——版本与验证：原文“当前”“尚未实现”等表述均保留其快照语境。代码块完整保留原始命令、帮助和输出，本文没有执行固件构建、连接音频设备或验证互操作性。

> 译注——术语：CSIP 为协调集标识配置文件（Coordinated Set Identification Profile）；CSIS 为协调集标识服务（Coordinated Set Identification Service）。`BT_MAX_CONN` 与 `BT_MAX_PAIRED` 是原文采用的符号写法，配置文件中应对照相应 `CONFIG_` 选项与所用版本。

本文说明如何以客户端和服务端两种角色运行协调集标识（coordinated set identification）功能。下方示例按原文删去了部分调试行，以缩短篇幅并便于理解整体流程。

<a id="set-coordinator-client"></a>

## 58.1 集合协调方（Set Coordinator，客户端）

客户端通常是资源较充足的设备，例如智能手机或笔记本电脑，可以锁定和释放协调集中的成员。协调集被锁定时，其他客户端不能再锁定该集合。

要锁定集合，客户端必须连接希望锁定的每个成员。此实现始终尝试同时连接集合中的所有成员。因此，若集合大小为 3，`BT_MAX_CONN` 至少应为 3。

若要在断开连接后继续保留成员的锁，必须与成员建立绑定（bond）。需要绑定多个成员时，应正确配置 `BT_MAX_PAIRED`。

<a id="using-the-set-coordinator"></a>

### 58.1.1 使用集合协调方（Using the Set Coordinator）

蓝牙协议栈完成初始化（`bt init`）且已连接集合成员设备后，原文称可调用 `csip_set_coordinator init` 初始化“通话控制客户端”，开始发现“TBS UUID”、保存句柄，并可选地订阅所有通知（默认全部订阅）。

> 译注——复制文字与命令版本：本节讨论 CSIP 集合协调方，服务为 CSIS，并非 TBS 通话控制。当前读取的[官方源码](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/audio/shell/csip_set_coordinator.c)及本仓库的[相对路径对照](../../../subsys/bluetooth/audio/shell/csip_set_coordinator.c)注册的是 `discover` 子命令，调用 `bt_csip_set_coordinator_discover()`；其帮助文本明确写为发现 CSIS。原页示例中的 `init`、`discover_sets` 与当前命令表不同，作为原文历史交互保留。实际使用前应先检查目标固件的 `csip_set_coordinator --help`，不可把两种版本的命令直接混用。

客户端连接并发现句柄后，可以读取用于识别其他集合成员的集合信息，然后扫描并连接其余成员。连接所有成员后，即可锁定与释放集合。

要正确使用集合协调方，必须启用 [`CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DBG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CSIP_SET_COORDINATOR_LOG_LEVEL_DBG)。

```text
csip_set_coordinator --help
csip_set_coordinator - Bluetooth CSIP_SET_COORDINATOR shell commands
Subcommands:
   init              :Initialize CSIP_SET_COORDINATOR
   discover          :Run discover for CSIS on peer device [member_index]
   discover_members  :Scan for set members <set_pointer>
   lock_set          :Lock set
   release_set       :Release set
   lock              :Lock specific member [member_index]
   release           :Release specific member [member_index]
   lock_get          :Get the lock value of the specific member and instance
                     [member_index [inst_idx]]
```

<a id="example-usage"></a>

### 58.1.2 使用示例（Example usage）

<a id="setup"></a>

#### 58.1.2.1 准备（Setup）

```text
uart:~$ init
uart:~$ bt connect P:xx:xx:xx:xx:xx:xx
```

<a id="when-connected"></a>

#### 58.1.2.2 已连接时（When connected）

发现设备上的集合：

```text
uart:~$ csip_set_coordinator init
<dbg> bt_csip_set_coordinator.primary_discover_func: [ATTRIBUTE] handle 0x0048
<dbg> bt_csip_set_coordinator.primary_discover_func: Discover complete, found 1 instances
<dbg> bt_csip_set_coordinator.discover_func: Setup complete for 1 / 1
Found 1 sets on device
uart:~$ csip_set_coordinator discover_sets
<dbg> bt_csip_set_coordinator.SIRK
36 04 9a dc 66 3a a1 a1 |6...f:..
1d 9a 2f 41 01 73 3e 01 |../A.s>.
<dbg> bt_csip_set_coordinator.csip_set_coordinator_discover_sets_read_set_size_cb: 2
<dbg> bt_csip_set_coordinator.csip_set_coordinator_discover_sets_read_set_lock_cb: 1
<dbg> bt_csip_set_coordinator.csip_set_coordinator_discover_sets_read_rank_cb: 1
Set size 2 (pointer: 0x566fdfe8)
```

根据上文集合指针发现集合成员：

```text
uart:~$ csip_set_coordinator discover_members 0x566fdfe8
<dbg> bt_csip_set_coordinator.csip_found: Found CSIS advertiser with address P:34:02:86:03:86:c0
<dbg> bt_csip_set_coordinator.is_set_member: hash: 0x33ccb1, prand 0x5bfe6a
<dbg> bt_csip_set_coordinator.is_discovered: P:34:02:86:03:86:c0
<dbg> bt_csip_set_coordinator.is_discovered: P:34:13:e8:b3:7f:9e
<dbg> bt_csip_set_coordinator.csip_found: Found member (2 / 2)
Discovered 2/2 set members
```

锁定集合成员：

```text
uart:~$ csip_set_coordinator lock_set
<dbg> bt_csip_set_coordinator.bt_csip_set_coordinator_lock_set: Connecting to P:34:02:86:03:86:c0
<dbg> bt_csip_set_coordinator.csip_set_coordinator_connected: Connected to P:34:02:86:03:86:c0
<dbg> bt_csip_set_coordinator.discover_func: Setup complete for 1 / 1
<dbg> bt_csip_set_coordinator.csip_set_coordinator_lock_set_init_cb:
<dbg> bt_csip_set_coordinator.SIRK
36 04 9a dc 66 3a a1 a1 |6...f:..
1d 9a 2f 41 01 73 3e 01 |../A.s>.
<dbg> bt_csip_set_coordinator.csip_set_coordinator_discover_sets_read_set_size_cb: 2
<dbg> bt_csip_set_coordinator.csip_set_coordinator_discover_sets_read_set_lock_cb: 1
<dbg> bt_csip_set_coordinator.csip_set_coordinator_discover_sets_read_rank_cb: 2
<dbg> bt_csip_set_coordinator.csip_set_coordinator_write_lowest_rank: Locking member with rank 1
<dbg> bt_csip_set_coordinator.notify_func: Instance 0 lock was locked
<dbg> bt_csip_set_coordinator.csip_set_coordinator_write_lowest_rank: Locking member with rank 2
<dbg> bt_csip_set_coordinator.notify_func: Instance 0 lock was locked
Set locked
```

释放集合成员：

```text
uart:~$ csip_set_coordinator release_set
<dbg> bt_csip_set_coordinator.csip_set_coordinator_release_highest_rank: Releasing member with rank 2
<dbg> bt_csip_set_coordinator.notify_func: Instance 0 lock was released
<dbg> bt_csip_set_coordinator.csip_set_coordinator_release_highest_rank: Releasing member with rank 1
<dbg> bt_csip_set_coordinator.notify_func: Instance 0 lock was released
Set released
```

<a id="coordinated-set-member-server"></a>

## 58.2 协调集成员（Coordinated Set Member，服务端）

服务端位于至少由两台设备组成的集合成员上，例如一对耳塞。

<a id="using-the-set-member"></a>

### 58.2.1 使用集合成员（Using the Set Member）

```text
csip_set_member --help
csip_set_member - Bluetooth CSIP set member shell commands
   Subcommands:
   register           : Initialize the service and register callbacks [size
                        <int>] [rank <int>] [not-lockable] [sirk <data>]
   lock               : Lock the set
   release            : Release the set [force]
   sirk               : Set the currently used SIRK <sirk>
   set_size_and_rank  : Set the currently used size and rank <size> <rank>
   get_info           : Get service info
   sirk_rsp           : Set the response used in SIRK requests <accept,
                        accept_enc, reject, oob>
```

<a id="id1"></a>

### 58.2.2 使用示例（Example Usage）

<a id="id2"></a>

#### 58.2.2.1 准备（Setup）

```text
uart:~$ bt init
uart:~$ csip_set_member register
```

<a id="setting-a-new-sirk"></a>

#### 58.2.2.2 设置新的 SIRK（Setting a new SIRK）

该命令可以修改当前使用的集合标识解析密钥（Set Identity Resolving Key，SIRK）。要在无线广播中使用新的可解析集合标识符（Resolvable Set Identifier，RSI），必须再次调用 `bt adv-data` 或 `bt advertise`，设置新的广播数据。如果启用了 `CONFIG_BT_CSIP_SET_MEMBER_SIRK_NOTIFIABLE`，也会通知已连接客户端。

```text
uart:~$ csip_set_member sirk 00112233445566778899aabbccddeeff
SIRK updated
```

<a id="setting-a-new-set-size-and-rank"></a>

#### 58.2.2.3 设置新的集合大小与秩（Setting a new set size and rank）

该命令可以修改服务实例的集合大小（set size）与秩（rank）。应同时对集合内所有设备进行此操作，且所有设备必须使用相同的集合大小。如果集合不可锁定，则忽略 rank；否则 rank 必须小于或等于集合大小，并且在该集合中对这台设备保持唯一。

```text
uart:~$ csip_set_member set_size_and_rank 1 1
Set size and rank updated to 1 and 1
```

<a id="getting-the-current-info"></a>

#### 58.2.2.4 获取当前信息（Getting the current info）

该命令可以获取当前使用的集合信息。

```text
uart:~$ csip_set_member get_info
Info for 0x2003b0c8
        SIRK
00000000: 20 37 0a 00 95 c4 04 20  00 00 00 00 f1 79 09 00 | 7.....  .....y..|
        Set size: 2
        Rank: 1
        Lockable: true
        Locked: false
```

对应官方文档源码：[doc/services/connectivity/bluetooth/shell/audio/csip.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/audio/csip.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/shell/audio/csip.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件或连接音频设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：通话控制配置文件CCP_Shell](P057_通话控制配置文件CCP_Shell.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：游戏音频配置文件GMAP_Shell](P059_游戏音频配置文件GMAP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P057_通话控制配置文件CCP_Shell.md) · [返回大纲](大纲.md) · [下一章](P059_游戏音频配置文件GMAP_Shell.md)

</details>

<!-- reading-navigation:end -->

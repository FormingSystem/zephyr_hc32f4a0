---
id: learning.zephyr-docs.bluetooth.page-106
title: Mesh_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/shell.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-mesh-shell"></a>

<a id="id1"></a>

# 第106章\_蓝牙 Mesh Shell（Bluetooth Mesh Shell）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/shell.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——执行环境：本章命令运行在设备固件提供的 Zephyr Shell 中，不是在主机的 Bash、PowerShell 或 Windows 命令提示符中运行。原例的 `uart:~$` 是设备提示符，输入时只输入其后的命令。前提是已取得并运行具有相应功能的 Mesh Shell 固件并连接其 Shell 后端；本次仅翻译文档，没有构建固件或连接设备。命令可用性以设备上不带参数的 `mesh` 输出为准，原文旧命令与当前源码差异在对应位置注明。

蓝牙 Mesh Shell 子系统为 [Shell 模块](../interaction/P001_Shell命令行.md#shell-api)提供一组 Mesh 命令，允许通过交互界面测试和探索蓝牙 Mesh API，无需另外编写应用程序。

该界面可访问大多数蓝牙 Mesh 功能，包括配网（Provisioning）、配置（Configuration）和消息发送（Message sending）。

<a id="prerequisites"></a>

## 106.1 前提条件（Prerequisites）

Mesh Shell 子系统依赖应用创建组成数据（Composition Data）并完成 Mesh 初始化。

> 译注——源码跟踪：原文所述应用组成与初始化，可从本仓库[官方测试应用 main.c](../../../tests/bluetooth/mesh_shell/src/main.c)中的 `root_models`、元素和初始化流程查看。当前官方 Shell 实现已按功能拆到[Shell 源码目录](../../../subsys/bluetooth/mesh/shell/)；它与本页后文保留的旧路径不同。相对路径只用于对照源码，实际运行步骤仍属于读者自己的固件工程。

<a id="application"></a>

## 106.2 应用程序（Application）

最方便的使用方式是运行 `tests/bluetooth/mesh_shell` 下的 Mesh Shell 应用。连接及交互方法见 [Shell 模块](../interaction/P001_Shell命令行.md#shell-api)说明。

<a id="basic-usage"></a>

## 106.3 基本使用（Basic usage）

该子系统新增一个 `mesh` 命令，并在其下组织各个子命令。每次设备启动后，都要先调用 `mesh init`，才能使用其他 Mesh Shell 命令：

```text
uart:~$ mesh init
```

这样做是为了确保所有可用日志都打印到 Shell 输出中。

<a id="provisioning"></a>

### 106.3.1 配网（Provisioning）

Mesh 节点必须经过配网才能加入网络。通常只需在设备首次启动时执行，因为设备会在重启之间保存配网数据。

最简单的方法是自配网（Self-provisioning）。使用默认网络密钥和地址 `0x0001` 为本设备配网，执行：

```text
uart:~$ mesh prov local 0 0x0001
```

所有节点使用相同的默认网络密钥，因此可以在多个设备上执行，只要为它们分配互不重叠的单播地址。要加入现有网络，也可用 `mesh prov pb-adv on` 或 `mesh prov pb-gatt on` 启用未配网信标（Unprovisioned beacon），由外部配网器（Provisioner）发现后将节点加入其网络。

> 译注——示例前提：这里使用的是官方测试示例默认值，自配网还要满足后文的 CDB 前提；不能给不同设备重复分配同一单播地址范围。`mesh target` 改变的是后续 Shell 消息的目标上下文，不会替节点完成配网、添加密钥或绑定模型。

节点加入网络后，可通过通用配置命令控制发送参数：

- 调用 `mesh target dst <Addr>` 设置目标地址。

- 调用 `mesh target net <NetKeyIdx>` 设置网络密钥索引。

- 调用 `mesh target app <AppKeyIdx>` 设置应用密钥索引。

默认使用配网时设置的地址和网络密钥发送消息。

<a id="configuration"></a>

### 106.3.2 配置（Configuration）

将目标地址设为本地单播地址（上面 `mesh prov local` 命令中的 `0x0001`），即可使用[模型（Models）](#bluetooth-mesh-shell-cfg-cli)命令对自身进行配置。

建议先读取节点自己的组成数据：

```text
uart:~$ mesh models cfg get-comp
```

该命令打印节点的组成数据，包括模型 ID 列表。

设备默认没有应用密钥，接下来可以添加一个：

```text
uart:~$ mesh models cfg appkey add 0 0
```

<a id="message-sending"></a>

### 106.3.3 消息发送（Message sending）

添加应用密钥后（见上文），节点的传输参数即已具备，Mesh Shell 可以通过网络发送原始 Mesh 消息。

例如，发送通用开关设置（Generic OnOff Set）消息：

```text
uart:~$ mesh test net-send 82020100
```

注意（Note）

除操作码（Opcode）之外，模型消息中的多字节字段均采用小端序（Little-endian）。

> 译注——示例载荷：原例 `82020100` 保留为一段连续十六进制字符串，其中 `82 02` 是操作码，后续字节是消息参数。发送成功不保证接收设备具有相应模型或已完成应用密钥绑定；模型必须具备匹配的操作码处理器。

消息发送到当前目标地址，使用当前网络密钥和应用密钥索引。默认目标是本地单播地址，因此设备只向自身发送。要改成所有节点广播地址（All Nodes），执行：

```text
uart:~$ mesh target dst 0xffff
```

目标地址设为 `0xffff` 后，网络中其他具有所配置网络密钥和应用密钥的节点都可以接收并处理这些消息。

注意（Note）

要修改本设备配置，必须在发出配置命令前将目标地址恢复为本地单播地址。

在开发过程中，发送原始 Mesh 包便于测试模型消息处理器，无需先实现发送模型。默认只能用这种方式测试模型消息的接收，因为 Mesh Shell 仅包含基础模型（Foundation model）。要在本节点接收数据包，需要在 `subsys/bluetooth/mesh/shell.c` 的组成数据中加入一个具有有效操作码处理器列表的模型，并在处理回调中将收到的消息打印到 Shell。

> 译注——旧源码位置：原文 `subsys/bluetooth/mesh/shell.c` 是旧布局。本次读取的[官方测试应用](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/tests/bluetooth/mesh_shell/src/main.c)在 `tests/bluetooth/mesh_shell/src/main.c` 定义模型组成；[官方 Shell 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/shell/shell.c)位于 `subsys/bluetooth/mesh/shell/shell.c`。应对照所用版本修改相应应用组成，不因旧路径不存在就新建一个同名旧文件。

<a id="parameter-formats"></a>

## 106.4 参数格式（Parameter formats）

Mesh Shell 命令支持以下参数格式：

<a id="id3"></a>

**参数格式（Parameter formats）**

| 类型（Type） | 说明（Description） | 示例（Example） |
| --- | --- | --- |
| 整数（Integers） | 未另行说明时使用的默认格式，可以是十进制或十六进制。 | `1234`, `0xabcd01234` |
| 十六进制字符串（Hexstrings） | UUID、密钥值、消息载荷等原始字节数组，应使用连续、不带前缀的十六进制字符串。 | `deadbeef01234` |
| 布尔值（Booleans） | API 文档使用 `<val(off, on)>` 表示布尔值。 | `on`, `off`, `enabled`, `disabled`, `1`, `0` |

<a id="commands"></a>

## 106.5 命令（Commands）

Mesh Shell 提供大量命令。部分命令接受参数，参数在命令名后用括号标示，例如 `mesh lpn set <value: off, on>`。尖括号表示必填参数，例如 `<NetKeyIdx>`；方括号表示可选参数，例如 `[DstAddr]`。

命令分为以下几组：

<a id="contents"></a>

- <a id="id4"></a>

  [通用配置（General configuration）](#general-configuration)

- <a id="id5"></a>

  [目标（Target）](#target)

- <a id="id6"></a>

  [低功耗节点（Low Power Node）](#low-power-node)

- <a id="id7"></a>

  [测试（Testing）](#testing)

- <a id="id8"></a>

  [配网（Provisioning）](#id2)

- <a id="id9"></a>

  [代理（Proxy）](#proxy)

- <a id="id10"></a>

  [模型（Models）](#models)

- <a id="id11"></a>

  [配置数据库（Configuration database）](#configuration-database)

- <a id="id12"></a>

  [统计（Statistic）](#statistic)

注意（Note）

部分命令依赖应用编译时启用的功能，并非所有功能都默认启用。不带参数执行 `mesh`，可以列出当前可用的命令。

<a id="general-configuration"></a>

### 106.5.1 [通用配置（General configuration）](#id4)

<a id="mesh-init"></a>

#### 106.5.1.1 `mesh init`

> 初始化 Mesh Shell。必须先执行此命令，才能使用其他 Mesh 命令。

<a id="mesh-reset-local"></a>

#### 106.5.1.2 `mesh reset-local`

> 将本地节点重置为初始未配网状态。如果存在配置数据库（Configuration Database，CDB），也会一并清除。

<a id="target"></a>

### 106.5.2 [目标（Target）](#id5)

目标命令用于查看和设置 Shell 的目标地址、网络索引和应用索引。配网、配置客户端等多种命令都会使用这些参数。

<a id="mesh-target-dst-dstaddr"></a>

#### 106.5.2.1 `mesh target dst [DstAddr]`

> 获取或设置消息目标地址。该地址决定通过 Shell 发送的 Mesh 包发往何处，不影响 Shell 控制范围之外的模块。
>
> - `DstAddr`：提供时设置新的 16 位目标地址；省略时打印当前目标地址。

<a id="mesh-target-net-netkeyidx"></a>

#### 106.5.2.2 `mesh target net [NetKeyIdx]`

> 获取或设置消息网络索引。它决定通过 Shell 发送的 Mesh 包使用哪一网络密钥加密，不影响 Shell 控制范围之外的模块。该密钥必须已经通过配网或配置客户端加入设备。
>
> - `NetKeyIdx`：提供时设置新的网络索引；省略时打印当前网络索引。

<a id="mesh-target-app-appkeyidx"></a>

#### 106.5.2.3 `mesh target app [AppKeyIdx]`

> 获取或设置消息应用索引。它决定通过 Shell 发送的 Mesh 包使用哪一应用密钥加密，不影响 Shell 控制范围之外的模块。应用密钥必须已由配置客户端加入设备，并绑定到当前网络索引。
>
> - `AppKeyIdx`：提供时设置新的应用索引；省略时打印当前应用索引。

<a id="low-power-node"></a>

### 106.5.3 [低功耗节点（Low Power Node）](#id6)

<a id="mesh-lpn-set-val-off-on"></a>

#### 106.5.3.1 `mesh lpn set <Val(off, on)>`

> 启用或禁用低功耗工作模式。启用后，设备关闭无线电并开始轮询 Friend 节点。
>
> - `Val`：设置是否启用低功耗模式。

<a id="mesh-lpn-poll"></a>

#### 106.5.3.2 `mesh lpn poll`

> 向 Friend 节点发起一次轮询，以接收待处理消息。仅在启用 LPN 时可用。

<a id="testing"></a>

### 106.5.4 [测试（Testing）](#id7)

<a id="mesh-test-net-send-hexstring"></a>

#### 106.5.4.1 `mesh test net-send <HexString>`

> 按当前目标地址、网络索引和应用索引发送原始 Mesh 消息。消息操作码必须手动编码。
>
> - `HexString`：待发送消息的原始十六进制表示。

<a id="mesh-test-iv-update"></a>

#### 106.5.4.2 `mesh test iv-update`

> 强制执行 IV 更新（IV Update）。

<a id="mesh-test-iv-update-test-val-off-on"></a>

#### 106.5.4.3 `mesh test iv-update-test <Val(off, on)>`

> 设置 IV 更新测试模式。测试模式会绕过 IV 更新的时序要求。
>
> - `Val`：启用或禁用 IV 更新测试模式。

<a id="mesh-test-rpl-clear"></a>

#### 106.5.4.4 `mesh test rpl-clear`

> 清空重放保护列表（Replay Protection List，RPL），使节点忘记此前接收的全部消息。

警告（Warning）

清空重放保护列表会破坏节点的安全机制，使其容易遭受消息重放攻击。绝不能在实际部署的网络中执行这一操作。

<a id="health-server-test"></a>

#### 106.5.4.5 健康服务端测试（Health Server Test）

<a id="mesh-test-health-srv-add-fault-faultid"></a>

##### 106.5.4.5.1 `mesh test health-srv add-fault <FaultID>`

> 为 Linux Foundation 公司标识注册一个新的健康服务端故障（Health Server Fault）。
>
> - `FaultID`：要注册的故障 ID（`0x0001` 至 `0xFFFF`）。

> 译注——故障 ID 宽度：原文范围写为 `0x0001` 至 `0xFFFF`，但本次[官方 Shell 实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/shell/shell.c)的 `cmd_add_fault()` 使用 `uint8_t fault_id` 并要求非零。这里按原文保留范围，实际应使用该版本支持的非零 8 位故障 ID（1—255），不要依赖超出宽度后可能发生的截断。对应本地[实现](../../../subsys/bluetooth/mesh/shell/shell.c)。

<a id="mesh-test-health-srv-del-fault-faultid"></a>

##### 106.5.4.5.2 `mesh test health-srv del-fault [FaultID]`

> 移除 Linux Foundation 公司标识下已注册的健康服务端故障。
>
> - `FaultID`：提供时删除指定故障；省略时清空所有已注册故障。

<a id="id2"></a>

### 106.5.5 [配网（Provisioning）](#id8)

要广播可连接的未配网信标，必须同时启用 [`CONFIG_BT_MESH_PROVISIONEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROVISIONEE) 和 [`CONFIG_BT_MESH_PB_GATT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PB_GATT)。

<a id="mesh-prov-pb-gatt-val-off-on"></a>

#### 106.5.5.1 `mesh prov pb-gatt <Val(off, on)>`

> 开始或停止广播可连接的未配网信标。附近使用 GATT 的配网器可借助信标发现节点，并通过 GATT 承载（Bearer）完成配网。
>
> - `Val`：启用或禁用通过 GATT 配网。

要广播未配网信标，必须同时启用 [`CONFIG_BT_MESH_PROVISIONEE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROVISIONEE) 和 [`CONFIG_BT_MESH_PB_ADV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PB_ADV)。

<a id="mesh-prov-pb-adv-val-off-on"></a>

#### 106.5.5.2 `mesh prov pb-adv <Val(off, on)>`

> 开始或停止广播未配网信标。附近使用广播方式的配网器可借助信标发现节点，并通过广播承载完成配网。
>
> - `Val`：启用或禁用通过广播配网。

要为其他设备配网，必须启用 [`CONFIG_BT_MESH_PROVISIONER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROVISIONER) 和 [`CONFIG_BT_MESH_PB_ADV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PB_ADV)。

<a id="mesh-prov-remote-adv-uuid-1-16-hex-netkeyidx-addr-attdur-s"></a>

#### 106.5.5.3 `mesh prov remote-adv <UUID(1-16 hex)> <NetKeyIdx> <Addr> <AttDur(s)>`

> 将附近设备加入 Mesh 网络。本节点扫描具有指定 UUID 的未配网信标；发现后，以指定单播地址将设备加入网络，并向其提供 `NetKeyIdx` 指定的网络密钥。
>
> - `UUID`：未配网设备的 UUID。若十六进制字符串不足 16 字节，则填入数组的 N 个最高有效字节，其余部分补零。
>
> - `NetKeyIdx`：要提供给设备的网络密钥索引。
>
> - `Addr`：分配给未配网设备的首个单播地址。设备的每个元素占用一个地址，整个地址范围都必须可用。
>
> - `AttDur`：未配网设备执行身份提示的持续时间，单位秒，需设备支持该功能。详见[关注状态（Attention state）](P079_Mesh健康服务端.md#bluetooth-mesh-models-health-srv-attention)。

要通过 GATT 为其他设备配网，必须启用 [`CONFIG_BT_MESH_PROVISIONER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROVISIONER) 和 [`CONFIG_BT_MESH_PB_GATT_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PB_GATT_CLIENT)。

<a id="mesh-prov-remote-gatt-uuid-1-16-hex-netkeyidx-addr-attdur-s"></a>

#### 106.5.5.4 `mesh prov remote-gatt <UUID(1-16 hex)> <NetKeyIdx> <Addr> <AttDur(s)>`

> 将附近设备加入 Mesh 网络。本节点扫描具有指定 UUID 的 PB-GATT 可连接广播；发现后，以指定单播地址将设备加入网络，并向其提供 `NetKeyIdx` 指定的网络密钥。
>
> - `UUID`：未配网设备的 UUID。若十六进制字符串不足 16 字节，则填入数组的 N 个最高有效字节，其余部分补零。
>
> - `NetKeyIdx`：要提供给设备的网络密钥索引。
>
> - `Addr`：分配给未配网设备的首个单播地址。设备的每个元素占用一个地址，整个地址范围都必须可用。
>
> - `AttDur`：未配网设备执行身份提示的持续时间，单位秒，需设备支持该功能。详见[关注状态（Attention state）](P079_Mesh健康服务端.md#bluetooth-mesh-models-health-srv-attention)。

<a id="mesh-prov-uuid-uuid-1-16-hex"></a>

#### 106.5.5.5 `mesh prov uuid [UUID(1-16 hex)]`

> 获取或设置本节点在未配网信标中使用的 UUID。
>
> - `UUID`：提供时为新的 128 位 UUID；不足 16 字节时，填入数组的 N 个最高有效字节，其余补零。省略时打印当前 UUID。需要启用 [`CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE)。

<a id="mesh-prov-input-num-number"></a>

#### 106.5.5.6 `mesh prov input-num <Number>`

> 输入数字形式的带外（Out-of-band，OOB）认证值，仅在配网过程中 Shell 提示输入时有效。输入数字必须与另一配网参与方显示的数字相同。
>
> - `Number`：十进制认证数字。

<a id="mesh-prov-input-str-string"></a>

#### 106.5.5.7 `mesh prov input-str <String>`

> 输入字母数字形式的 OOB 认证值，仅在配网过程中 Shell 提示输入时有效。输入字符串必须与另一配网参与方显示的字符串相同。
>
> - `String`：不加引号的字母数字认证字符串。

<a id="mesh-prov-static-oob-val-1-32-hex"></a>

#### 106.5.5.8 `mesh prov static-oob [Val(1-32 hex)]`

> 设置或清除静态 OOB 认证值。必须在配网开始前设置才会生效，双方的静态 OOB 值必须相同。需要启用 [`CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE)。
>
> - `Val`：提供时为新的静态 OOB 十六进制值。不足 16 字节时填入数组的 N 个最高有效字节，其余补零；省略时清除静态 OOB 值。

> 译注——静态 OOB 长度：本页命令标题、参数正文在 16／32 字节上的表述并不一致。本次官方 `cmd_static_oob()` 最多转换 32 字节，并保存实际转换长度；`cmd_auth_method_set_static()` 同样使用 32 字节数组，并将实际长度交给认证接口。不能将“补零”说明理解成这两个处理函数都会自动把输入扩展为固定长度。以所用版本的命令处理及认证算法要求为准，双方必须采用一致的值和长度；源码见本章的[Shell 实现](../../../subsys/bluetooth/mesh/shell/shell.c)。

<a id="mesh-prov-local-netkeyidx-addr-ivi"></a>

#### 106.5.5.9 `mesh prov local <NetKeyIdx> <Addr> [IVI]`

> 对本节点自配网。启用配置数据库时，必须先创建网络密钥；否则使用默认密钥值。
>
> - `NetKeyIdx`：用于配网的网络密钥索引。
>
> - `Addr`：分配给设备的首个单播地址。设备的每个元素占用一个地址，整个地址范围都必须可用。
>
> - `IVI`：当前网络 IV 索引，省略时默认为 0。

<a id="mesh-prov-beacon-listen-val-off-on"></a>

#### 106.5.5.10 `mesh prov beacon-listen <Val(off, on)>`

> 启用或禁用收到未配网信标时的打印输出，使配网器能够发现附近未配网设备并为其配网。需要启用 [`CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE)。
>
> - `Val`：是否打印未配网信标。

<a id="mesh-prov-remote-pub-key-pubkey"></a>

#### 106.5.5.11 `mesh prov remote-pub-key <PubKey>`

> 提供设备公钥（Device public key）。
>
> - `PubKey`：采用大端序（Big-endian）的设备公钥。

<a id="mesh-prov-auth-method-input-action-size"></a>

#### 106.5.5.12 `mesh prov auth-method input <Action> <Size>`

> 在配网器上指定未配网设备使用的输入型 OOB（Input OOB）认证动作。
>
> - `Action`：输入动作，允许值如下：
>
>   > - `0`：不执行输入动作。
> >
> > - `1`：按压动作（Push）。
> >
> > - `2`：旋转动作（Twist）。
> >
> > - `4`：输入数字（Enter number）。
> >
> > - `8`：输入字符串（Enter String）。
>
> - `Size`：认证大小。

<a id="mesh-prov-auth-method-output-action-size"></a>

#### 106.5.5.13 `mesh prov auth-method output <Action> <Size>`

> 在配网器上指定未配网设备使用的输出型 OOB（Output OOB）认证动作。
>
> - `Action`：输出动作，允许值如下：
>
>   > - `0`：不执行输出动作。
> >
> > - `1`：闪烁动作（Blink）。
> >
> > - `2`：振动动作（Vibrate）。
> >
> > - `4`：显示数字（Display number）。
> >
> > - `8`：显示字符串（Display String）。
>
> - `Size`：认证大小。

> 译注——输出动作数值差异：下方保留原页列表，但本次[官方 main.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/mesh/main.h)枚举为 `BT_MESH_BLINK=1`、`BT_MESH_BEEP=2`、`BT_MESH_VIBRATE=4`、`BT_MESH_DISPLAY_NUMBER=8`、`BT_MESH_DISPLAY_STRING=16`。原列表漏掉蜂鸣（Beep），导致后续数值与源码不符。Shell 的 `cmd_auth_method_set_output()` 直接解析动作数值并传给认证接口，应按所用版本枚举选择；本仓库相对[头文件](../../../include/zephyr/bluetooth/mesh/main.h)可供核对。

<a id="mesh-prov-auth-method-static-val-1-16-hex"></a>

#### 106.5.5.14 `mesh prov auth-method static <Val(1-16 hex)>`

> 在配网器上要求未配网设备使用静态 OOB 认证，并在配网时使用给定的静态认证值。
>
> - `Val`：静态 OOB 值。不足 32 字节的十六进制字符串填入数组的 N 个最高有效字节，其余补零。

<a id="mesh-prov-auth-method-none"></a>

#### 106.5.5.15 `mesh prov auth-method none`

> 在配网器上为新设备配网时不使用认证。这是默认行为。

<a id="proxy"></a>

### 106.5.6 [代理（Proxy）](#id9)

代理服务端（Proxy Server）是可选子系统，通过 [`CONFIG_BT_MESH_GATT_PROXY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_GATT_PROXY) 启用。

<a id="mesh-proxy-identity-enable"></a>

#### 106.5.6.1 `mesh proxy identity-enable`

> 启用代理节点身份（Proxy Node Identity）信标，使代理设备能够明确选择连接本设备。该信标运行 60 秒后，节点恢复发送普通代理信标。

代理客户端（Proxy Client）是可选子系统，通过 [`CONFIG_BT_MESH_PROXY_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROXY_CLIENT) 启用。

<a id="mesh-proxy-connect-netkeyidx"></a>

#### 106.5.6.2 `mesh proxy connect <NetKeyIdx>`

> 自动连接附近的代理服务端以接入 Mesh。
>
> - `NetKeyIdx`：要连接的网络密钥索引。

<a id="mesh-proxy-disconnect-netkeyidx"></a>

#### 106.5.6.3 `mesh proxy disconnect <NetKeyIdx>`

> 断开已有代理连接。
>
> - `NetKeyIdx`：要断开的网络密钥索引。

<a id="mesh-proxy-solicit-netkeyidx"></a>

#### 106.5.6.4 `mesh proxy solicit <NetKeyIdx>`

> 对子网发起代理请求（Proxy Solicitation）。通过 [`CONFIG_BT_MESH_PROXY_SOLICITATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROXY_SOLICITATION) 启用此功能。
>
> - `NetKeyIdx`：发送请求 PDU 所用的网络密钥索引。

<a id="models"></a>

<a id="bluetooth-mesh-shell-cfg-cli"></a>

### 106.5.7 [模型（Models）](#id10)

<a id="configuration-client"></a>

#### 106.5.7.1 配置客户端（Configuration Client）

配置客户端模型是可选子系统，通过 [`CONFIG_BT_MESH_CFG_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CFG_CLI) 启用。在 `mesh models` 子命令列表中，它作为独立模块 `mesh models cfg` 实现。启用所述 Shell 配置选项、且应用的模型组成中包含配置客户端模型时，该模块可用于任意配置客户端模型实例，可配置自身或网络中的其他节点。

配置客户端使用 `mesh target dst` 和 `mesh target net` 设置的通用消息参数选择目标节点。如果启用了 [`CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SHELL_PROV_CTX_INSTANCE) 且已初始化 Shell 配网上下文，Shell 节点完成配网后，配置客户端默认以自身为目标；Shell 为其他节点完成配网后，则以新节点为目标。常见用法中，完整功能依赖配网功能和配置数据库。配置客户端始终使用绑定到目标地址的设备密钥（Device key）发送消息，因此只能配置自身和由它配网的节点。以下步骤演示如何准备设备以使用配置客户端命令：

- 初始化客户端节点（`mesh init`）。

- 创建 CDB（`mesh cdb create`）。

- 为本设备配网（`mesh prov local`）。

- 此时 Shell 模块应以自身为目标。

- 查看本地节点组成数据（`mesh models cfg get-comp`）。

- 按需使用配置客户端命令配置本地节点。

- 为其他设备配网（`mesh prov beacon-listen`、`mesh prov remote-adv`、`mesh prov remote-gatt`）。

- 此时 Shell 模块应以新加入的节点为目标。

- 查看新配网节点及其地址（`mesh cdb show`）。

- 查看目标设备组成数据（`mesh models cfg get-comp`）。

- 按需使用配置客户端命令配置该节点。

<a id="mesh-models-cfg-target-get"></a>

##### 106.5.7.1.1 `mesh models cfg target get`

> 获取配置客户端模型的目标配置服务端。

<a id="mesh-models-cfg-help"></a>

##### 106.5.7.1.2 `mesh models cfg help`

> 打印配置客户端 Shell 模块的信息。

<a id="mesh-models-cfg-reset"></a>

##### 106.5.7.1.3 `mesh models cfg reset`

> 重置目标设备。

<a id="mesh-models-cfg-timeout-timeout-s"></a>

##### 106.5.7.1.4 `mesh models cfg timeout [Timeout(s)]`

> 获取或设置配置客户端发送消息时使用的超时。
>
> - `Timeout`：提供时设置超时，单位秒；省略时打印当前超时。

<a id="mesh-models-cfg-get-comp-page"></a>

##### 106.5.7.1.5 `mesh models cfg get-comp [Page]`

> 读取组成数据页并完整打印。如果目标没有指定页，则返回该页之前的最后一页。
>
> - `Page`：请求的组成数据页，省略时默认为 0。

<a id="mesh-models-cfg-beacon-val-off-on"></a>

##### 106.5.7.1.6 `mesh models cfg beacon [Val(off, on)]`

> 获取或设置网络信标发送状态。
>
> - `Val`：提供时启用或禁用网络信标发送；省略时打印当前状态。

<a id="mesh-models-cfg-ttl-ttl"></a>

##### 106.5.7.1.7 `mesh models cfg ttl [TTL]`

> 获取或设置默认生存时间（Time to Live，TTL）。
>
> - `TTL`：提供时设置新的默认 TTL，有效值为 0x00 和 0x02—0x7f；省略时打印当前默认 TTL。

<a id="mesh-models-cfg-friend-val-off-on"></a>

##### 106.5.7.1.8 `mesh models cfg friend [Val(off, on)]`

> 获取或设置 Friend 功能。
>
> - `Val`：提供时启用或禁用 Friend 功能；省略时打印当前状态：
>
>   > - `0x00`：支持该功能，但未启用。
> >
> > - `0x01`：已启用该功能。
> >
> > - `0x02`：不支持该功能。

<a id="mesh-models-cfg-gatt-proxy-val-off-on"></a>

##### 106.5.7.1.9 `mesh models cfg gatt-proxy [Val(off, on)]`

> 获取或设置 GATT 代理（GATT Proxy）功能。
>
> - `Val`：提供时启用或禁用 GATT 代理；省略时打印当前状态：
>
>   > - `0x00`：支持该功能，但未启用。
> >
> > - `0x01`：已启用该功能。
> >
> > - `0x02`：不支持该功能。

<a id="mesh-models-cfg-relay-val-off-on-count-int-ms"></a>

##### 106.5.7.1.10 `mesh models cfg relay [<Val(off, on)> [<Count> [Int(ms)]]]`

> 获取或设置中继（Relay）功能及其参数。
>
> - `Val`：提供时启用或禁用中继功能；省略时打印当前状态：
>
>   > - `0x00`：支持该功能，但未启用。
> >
> > - `0x01`：已启用该功能。
> >
> > - `0x02`：不支持该功能。
>
> - `Count`：`val` 为 `on` 时设置中继重传次数，合法范围为 0—7，省略时默认为 `2`；`val` 为 `off` 时忽略此参数。
>
> - `Int`：`val` 为 `on` 时设置中继重传间隔，单位毫秒，合法范围为 10—320，省略时默认为 `20`；`val` 为 `off` 时忽略。

<a id="mesh-models-cfg-node-id-netkeyidx-identity"></a>

##### 106.5.7.1.11 `mesh models cfg node-id <NetKeyIdx> [Identity]`

> 获取或设置子网当前的节点身份（Node Identity）状态。
>
> - `NetKeyIdx`：要获取／设置状态的网络密钥索引。
>
> - `Identity`：提供时设置节点身份状态值。

<a id="mesh-models-cfg-polltimeout-get-lpnaddr"></a>

##### 106.5.7.1.12 `mesh models cfg polltimeout-get <LPNAddr>`

> 获取 Friend 节点中指定 LPN 的轮询超时（PollTimeout）计时器当前值。
>
> - `LPNAddr`：低功耗节点地址。

<a id="mesh-models-cfg-net-transmit-param-count-int-ms"></a>

##### 106.5.7.1.13 `mesh models cfg net-transmit-param [<Count> <Int(ms)>]`

> 获取或设置网络发送参数。
>
> - `Count`：每条已发送消息的额外网络发送次数，合法范围为 0—7。
>
> - `Int`：新的网络重传间隔，单位毫秒，合法范围为 10—320。

<a id="mesh-models-cfg-netkey-add-netkeyidx-key-1-16-hex"></a>

##### 106.5.7.1.14 `mesh models cfg netkey add <NetKeyIdx> [Key(1-16 hex)]`

> 向目标节点添加网络密钥。如果启用了 CDB，也会加入配置数据库。
>
> - `NetKeyIdx`：要添加的网络密钥索引。
>
> - `Key`：提供时设置 128 位十六进制密钥值；不足 16 字节时填入数组的 N 个最高有效字节，其余补零。仅当 CDB 中尚无该密钥时有效。省略时使用默认密钥值。

<a id="mesh-models-cfg-netkey-upd-netkeyidx-key-1-16-hex"></a>

##### 106.5.7.1.15 `mesh models cfg netkey upd <NetKeyIdx> [Key(1-16 hex)]`

> 更新目标节点的网络密钥。
>
> - `NetKeyIdx`：要更新的网络密钥索引。
>
> - `Key`：提供时设置 128 位十六进制密钥值；不足 16 字节时填入数组的 N 个最高有效字节，其余补零。省略时使用默认密钥值。

<a id="mesh-models-cfg-netkey-get"></a>

##### 106.5.7.1.16 `mesh models cfg netkey get`

> 获取已知网络密钥索引列表。

<a id="mesh-models-cfg-netkey-del-netkeyidx"></a>

##### 106.5.7.1.17 `mesh models cfg netkey del <NetKeyIdx>`

> 从目标节点删除网络密钥。
>
> - `NetKeyIdx`：要删除的网络密钥索引。

<a id="mesh-models-cfg-appkey-add-netkeyidx-appkeyidx-key-1-16-hex"></a>

##### 106.5.7.1.18 `mesh models cfg appkey add <NetKeyIdx> <AppKeyIdx> [Key(1-16 hex)]`

> 向目标节点添加应用密钥。如果启用了 CDB，也会加入配置数据库。
>
> - `NetKeyIdx`：应用密钥所绑定的网络密钥索引。
>
> - `AppKeyIdx`：要添加的应用密钥索引。
>
> - `Key`：提供时设置 128 位十六进制密钥值；不足 16 字节时填入数组的 N 个最高有效字节，其余补零。仅当 CDB 中尚无该密钥时有效。省略时使用默认密钥值。

<a id="mesh-models-cfg-appkey-upd-netkeyidx-appkeyidx-key-1-16-hex"></a>

##### 106.5.7.1.19 `mesh models cfg appkey upd <NetKeyIdx> <AppKeyIdx> [Key(1-16 hex)]`

> 更新目标节点的应用密钥。
>
> - `NetKeyIdx`：应用密钥所绑定的网络密钥索引。
>
> - `AppKeyIdx`：要更新的应用密钥索引。
>
> - `Key`：提供时设置 128 位十六进制密钥值；不足 16 字节时填入数组的 N 个最高有效字节，其余补零。省略时使用默认密钥值。

<a id="mesh-models-cfg-appkey-get-netkeyidx"></a>

##### 106.5.7.1.20 `mesh models cfg appkey get <NetKeyIdx>`

> 获取绑定到指定网络密钥索引的已知应用密钥索引列表。
>
> - `NetKeyIdx`：要查询其应用密钥索引列表的网络密钥索引。

<a id="mesh-models-cfg-appkey-del-netkeyidx-appkeyidx"></a>

##### 106.5.7.1.21 `mesh models cfg appkey del <NetKeyIdx> <AppKeyIdx>`

> 从目标节点删除应用密钥。
>
> - `NetKeyIdx`：应用密钥所绑定的网络密钥索引。
>
> - `AppKeyIdx`：要删除的应用密钥索引。

<a id="mesh-models-cfg-model-app-bind-addr-appkeyidx-mid-cid"></a>

##### 106.5.7.1.22 `mesh models cfg model app-bind <Addr> <AppKeyIdx> <MID> [CID]`

> 将应用密钥绑定到模型。模型只能加密和解密使用其已绑定应用密钥的消息。
>
> - `Addr`：模型所在元素的地址。
>
> - `AppKeyIdx`：要绑定到模型的应用密钥。
>
> - `MID`：要绑定密钥的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-app-unbind-addr-appkeyidx-mid-cid"></a>

##### 106.5.7.1.23 `mesh models cfg model app-unbind <Addr> <AppKeyIdx> <MID> [CID]`

> 解除模型与应用密钥的绑定。
>
> - `Addr`：模型所在元素的地址。
>
> - `AppKeyIdx`：要从模型解除绑定的应用密钥。
>
> - `MID`：要解除密钥绑定的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-app-get-elemaddr-mid-cid"></a>

##### 106.5.7.1.24 `mesh models cfg model app-get <ElemAddr> <MID> [CID]`

> 获取模型绑定的应用密钥列表。
>
> - `ElemAddr`：模型所在元素的地址。
>
> - `MID`：要查询绑定密钥的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-pub-addr-mid-cid-pubaddr-appkeyidx-cred-off-on-ttl-perres-persteps-count-int-ms"></a>

##### 106.5.7.1.25 `mesh models cfg model pub <Addr> <MID> [CID] [<PubAddr> <AppKeyIdx> <Cred(off, on)> <TTL> <PerRes> <PerSteps> <Count> <Int(ms)>]`

> 获取或设置模型发布（Publication）参数。提供全部发布参数时，将其设为新参数；全部省略时，打印当前发布参数。
>
> - `Addr`：模型所在元素的地址。
>
> - `MID`：要查询绑定密钥的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。
>
> 发布参数：
>
> > - `PubAddr`：发布消息的目标地址。
> >
> > - `AppKeyIdx`：发布消息使用的应用密钥索引。
> >
> > - `Cred`：作为低功耗节点时，是否使用友谊凭据（Friendship credentials）发布。
> >
> > - `TTL`：发布消息使用的 TTL（`0x00` 至 `0x07f`）。
> >
> > - `PerRes`：发布周期步长的分辨率：
> >
> >   > - `0x00`：每步 100 毫秒。
> > >
> > > - `0x01`：每步 1 秒。
> > >
> > > - `0x02`：每步 10 秒。
> > >
> > > - `0x03`：每步 10 分钟。
> >
> > - `PerSteps`：发布周期包含的步数；0 表示禁用周期发布。
> >
> > - `Count`：每条发布消息的重传次数（`0` 至 `7`）。
> >
> > - `Int`：重传间隔，单位毫秒，必须是 50 的整数倍。

> 译注——编码范围不是全部合法取值：本页一些 TTL 参数使用连续区间简写，而前面的默认 TTL 条目明确排除了 1。不要据此把区间中的每个数字都当作有效值；模型发布参数的含义与校验仍取决于对应配置接口。

<a id="mesh-models-cfg-model-pub-va-addr-uuid-1-16-hex-appkeyidx-cred-off-on-ttl-perres-persteps-count-int-ms-mid-cid"></a>

##### 106.5.7.1.26 `mesh models cfg model pub-va <Addr> <UUID(1-16 hex)> <AppKeyIdx> <Cred(off, on)> <TTL> <PerRes> <PerSteps> <Count> <Int(ms)> <MID> [CID]`

> 设置模型的发布参数。
>
> - `Addr`：模型所在元素的地址。
>
> - `MID`：要查询绑定密钥的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。
>
> 发布参数：
>
> > - `UUID`：发布的目标虚拟地址。十六进制字符串不足 16 字节时填入数组的 N 个最高有效字节，其余补零。
> >
> > - `AppKeyIdx`：发布消息使用的应用密钥索引。
> >
> > - `Cred`：作为低功耗节点时，是否使用友谊凭据（Friendship credentials）发布。
> >
> > - `TTL`：发布消息使用的 TTL（`0x00` 至 `0x07f`）。
> >
> > - `PerRes`：发布周期步长的分辨率：
> >
> >   > - `0x00`：每步 100 毫秒。
> > >
> > > - `0x01`：每步 1 秒。
> > >
> > > - `0x02`：每步 10 秒。
> > >
> > > - `0x03`：每步 10 分钟。
> >
> > - `PerSteps`：发布周期包含的步数；0 表示禁用周期发布。
> >
> > - `Count`：每条发布消息的重传次数（`0` 至 `7`）。
> >
> > - `Int`：重传间隔，单位毫秒，必须是 50 的整数倍。

<a id="mesh-models-cfg-model-sub-add-elemaddr-subaddr-mid-cid"></a>

##### 106.5.7.1.27 `mesh models cfg model sub-add <ElemAddr> <SubAddr> <MID> [CID]`

> 将模型订阅到组地址。模型只接收发往自身单播地址、或其订阅的组地址／虚拟地址的消息。一个模型可以订阅多个组地址和虚拟地址。
>
> - `ElemAddr`：模型所在元素的地址。
>
> - `SubAddr`：要订阅的 16 位组地址（`0xc000` 至 `0xFEFF`）。
>
> - `MID`：要添加订阅的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-sub-del-elemaddr-subaddr-mid-cid"></a>

##### 106.5.7.1.28 `mesh models cfg model sub-del <ElemAddr> <SubAddr> <MID> [CID]`

> 取消模型对某个组地址的订阅。
>
> - `ElemAddr`：模型所在元素的地址。
>
> - `SubAddr`：要从订阅列表移除的 16 位组地址（`0xc000` 至 `0xFEFF`）。
>
> - `MID`：要添加订阅的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-sub-add-va-elemaddr-labeluuid-1-16-hex-mid-cid"></a>

##### 106.5.7.1.29 `mesh models cfg model sub-add-va <ElemAddr> <LabelUUID(1-16 hex)> <MID> [CID]`

> 将模型订阅到虚拟地址。模型只接收发往自身单播地址、或其订阅的组地址／虚拟地址的消息。一个模型可以订阅多个组地址和虚拟地址。
>
> - `ElemAddr`：模型所在元素的地址。
>
> - `LabelUUID`：所订阅虚拟地址的 128 位标签 UUID。十六进制字符串不足 16 字节时填入数组的 N 个最高有效字节，其余补零。
>
> - `MID`：要添加订阅的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-sub-del-va-elemaddr-labeluuid-1-16-hex-mid-cid"></a>

##### 106.5.7.1.30 `mesh models cfg model sub-del-va <ElemAddr> <LabelUUID(1-16 hex)> <MID> [CID]`

> 取消模型对某个虚拟地址的订阅。
>
> - `ElemAddr`：模型所在元素的地址。
>
> - `LabelUUID`：要取消订阅的虚拟地址对应的 128 位标签 UUID。十六进制字符串不足 16 字节时填入数组的 N 个最高有效字节，其余补零。
>
> - `MID`：要添加订阅的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-sub-ow-elemaddr-subaddr-mid-cid"></a>

##### 106.5.7.1.31 `mesh models cfg model sub-ow <ElemAddr> <SubAddr> <MID> [CID]`

> 用一个新的组地址覆盖模型的全部订阅。
>
> - `ElemAddr`：模型所在元素的地址。
>
> - `SubAddr`：要加入订阅列表的 16 位组地址（`0xc000` 至 `0xFEFF`）。
>
> - `MID`：要添加订阅的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-sub-ow-va-elemaddr-labeluuid-1-16-hex-mid-cid"></a>

##### 106.5.7.1.32 `mesh models cfg model sub-ow-va <ElemAddr> <LabelUUID(1-16 hex)> <MID> [CID]`

> 用一个新的虚拟地址覆盖模型的全部订阅。模型只接收发往自身单播地址、或其订阅的组地址／虚拟地址的消息。一个模型可以订阅多个组地址和虚拟地址。
>
> - `ElemAddr`：模型所在元素的地址。
>
> - `LabelUUID`：作为新订阅地址的虚拟地址所对应的 128 位标签 UUID。十六进制字符串不足 16 字节时填入数组的 N 个最高有效字节，其余补零。
>
> - `MID`：要添加订阅的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-sub-del-all-elemaddr-mid-cid"></a>

##### 106.5.7.1.33 `mesh models cfg model sub-del-all <ElemAddr> <MID> [CID]`

> 移除模型的全部组地址和虚拟地址订阅。
>
> - `ElemAddr`：模型所在元素的地址。
>
> - `MID`：要取消全部订阅的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-model-sub-get-elemaddr-mid-cid"></a>

##### 106.5.7.1.34 `mesh models cfg model sub-get <ElemAddr> <MID> [CID]`

> 获取模型订阅的地址列表。
>
> - `ElemAddr`：模型所在元素的地址。
>
> - `MID`：要查询订阅列表的模型 ID。
>
> - `CID`：提供时指定模型的公司标识（Company ID）；省略时表示 Bluetooth SIG 定义的模型。

<a id="mesh-models-cfg-krp-netkeyidx-phase"></a>

##### 106.5.7.1.35 `mesh models cfg krp <NetKeyIdx> [Phase]`

> 获取或设置子网的密钥刷新阶段（Key Refresh Phase）。
>
> - `NetKeyIdx`：用于获取／设置当前密钥刷新阶段的网络密钥索引。
>
> - `Phase`：新的密钥刷新阶段，有效值如下：
>
>   > - `0x00`：正常工作，未进行密钥刷新。
> >
> > - `0x01`：密钥刷新过程的第一阶段。
> >
> > - `0x02`：密钥刷新过程的第二阶段。

<a id="mesh-models-cfg-hb-sub-src-dst-per"></a>

##### 106.5.7.1.36 `mesh models cfg hb-sub [<Src> <Dst> <Per>]`

> 获取或设置心跳（Heartbeat）订阅参数。节点仅接收符合订阅参数的心跳消息。提供参数时设置，无参数调用时打印当前参数。
>
> - `Src`：接收心跳消息的单播源地址。
>
> - `Dst`：接收心跳消息的目标地址。
>
> - `Per`：以对数表示的心跳订阅时长：
>
>   > - `0`：禁用心跳订阅。
> >
> > - `1` 至 `17`：订阅心跳的时长为 2^(period - 1) 秒。

<a id="mesh-models-cfg-hb-pub-dst-count-per-ttl-features-netkeyidx"></a>

##### 106.5.7.1.37 `mesh models cfg hb-pub [<Dst> <Count> <Per> <TTL> <Features> <NetKeyIdx>]`

> 获取或设置心跳发布参数。提供参数时设置，无参数调用时打印当前参数。
>
> - `Dst`：心跳发布的目标地址。
>
> - `Count`：以对数表示的周期性心跳发布数量：
>
>   > - `0`：不周期性发布心跳。
> >
> > - `1` 至 `17`：周期性发布 2^(count - 1) 条心跳消息。
> >
> > - `255`：无限期周期性发布心跳消息。
>
> - `Per`：以对数表示的心跳发布周期：
>
>   > - `0`：不周期性发布心跳。
> >
> > - `1` 至 `17`：每隔 2^(period - 1) 秒发布一条心跳。
>
> - `TTL`：心跳消息的 TTL（`0x00` 至 `0x7f`）。
>
> - `Features`：状态变化时应触发心跳发布的功能位字段：
>
>   > - `Bit 0`：中继功能（Relay）。
> >
> > - `Bit 1`：代理功能（Proxy）。
> >
> > - `Bit 2`：Friend 功能。
> >
> > - `Bit 3`：低功耗功能（Low Power）。
>
> - `NetKeyIdx`：发布心跳消息使用的网络密钥索引。

<a id="health-client"></a>

#### 106.5.7.2 健康客户端（Health Client）

健康客户端模型是可选子系统，通过 [`CONFIG_BT_MESH_HEALTH_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_HEALTH_CLI) 启用。在 `mesh models` 子命令列表中，它作为独立模块 `mesh models health` 实现。启用所述 Shell 配置选项、且应用模型组成中包含一个或多个健康客户端时，该模块可用于任意健康客户端实例，用来触发 Mesh 网络设备上的健康客户端与服务端交互。

默认选择模型组成中的第一个健康客户端实例。可使用 `mesh models health instance set` 和 `mesh models health instance get-all` 选择指定实例。

健康客户端可使用 `mesh target dst`、`mesh target net` 和 `mesh target app` 设置的通用消息参数选择目标节点。如果 Shell 目标地址设为零，所选客户端会尝试按自身已配置的发布参数发布消息。

<a id="mesh-models-health-instance-set-elemidx"></a>

##### 106.5.7.2.1 `mesh models health instance set <ElemIdx>`

> 设置要使用的健康客户端模型实例。
>
> - `ElemIdx`：健康客户端模型所在的元素索引。

<a id="mesh-models-health-instance-get-all"></a>

##### 106.5.7.2.2 `mesh models health instance get-all`

> 打印设备上所有可用的健康客户端实例。

<a id="mesh-models-health-fault-get-cid"></a>

##### 106.5.7.2.3 `mesh models health fault-get <CID>`

> 获取指定公司标识下已注册的故障列表。
>
> - `CID`：要查询故障的公司标识。

<a id="mesh-models-health-fault-clear-cid"></a>

##### 106.5.7.2.4 `mesh models health fault-clear <CID>`

> 清除指定公司标识下的故障列表。
>
> - `CID`：要清除故障的公司标识。

<a id="mesh-models-health-fault-clear-unack-cid"></a>

##### 106.5.7.2.5 `mesh models health fault-clear-unack <CID>`

> 清除指定公司标识下的故障列表，不要求响应。
>
> - `CID`：要清除故障的公司标识。

<a id="mesh-models-health-fault-test-cid-testid"></a>

##### 106.5.7.2.6 `mesh models health fault-test <CID> <TestID>`

> 调用自测试（Self-test）过程，并显示触发的故障列表。
>
> - `CID`：要执行自测试的公司标识。
>
> - `TestID`：要执行的测试。

<a id="mesh-models-health-fault-test-unack-cid-testid"></a>

##### 106.5.7.2.7 `mesh models health fault-test-unack <CID> <TestID>`

> 调用自测试过程，不要求响应。
>
> - `CID`：要执行自测试的公司标识。
>
> - `TestID`：要执行的测试。

<a id="mesh-models-health-period-get"></a>

##### 106.5.7.2.8 `mesh models health period-get`

> 获取当前健康服务端发布周期除数（Publish period divisor）。

<a id="mesh-models-health-period-set-divisor"></a>

##### 106.5.7.2.9 `mesh models health period-set <Divisor>`

> 设置当前健康服务端发布周期除数。检测到故障后，健康服务端以更短间隔发布故障状态。间隔由该除数确定：故障发布周期 = 发布周期 / 2^divisor。
>
> - `Divisor`：新的健康服务端发布周期除数。

<a id="mesh-models-health-period-set-unack-divisor"></a>

##### 106.5.7.2.10 `mesh models health period-set-unack <Divisor>`

> 设置当前健康服务端发布周期除数。检测到故障后，健康服务端以更短间隔发布故障状态。间隔由该除数确定：故障发布周期 = 发布周期 / 2^divisor。
>
> - `Divisor`：新的健康服务端发布周期除数。

<a id="mesh-models-health-attention-get"></a>

##### 106.5.7.2.11 `mesh models health attention-get`

> 获取当前健康服务端关注状态（Attention state）。

<a id="mesh-models-health-attention-set-time-s"></a>

##### 106.5.7.2.12 `mesh models health attention-set <Time(s)>`

> 在指定时间内启用健康服务端关注状态。
>
> - `Time`：关注状态持续时间，单位秒（`0` 至 `255`）。

<a id="mesh-models-health-attention-set-unack-time-s"></a>

##### 106.5.7.2.13 `mesh models health attention-set-unack <Time(s)>`

> 在指定时间内启用关注状态，不要求响应。
>
> - `Time`：关注状态持续时间，单位秒（`0` 至 `255`）。

<a id="binary-large-object-blob-transfer-client-model"></a>

#### 106.5.7.3 二进制大对象传输客户端模型（Binary Large Object Transfer Client，BLOB）

启用 [`CONFIG_BT_MESH_BLOB_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BLOB_CLI) 并禁用 [`CONFIG_BT_MESH_DFU_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_DFU_CLI)，可将 BLOB 传输客户端加入 Mesh Shell。 相关链接：[大对象传输客户端（BLOB Transfer Client）](P099_Mesh大对象传输客户端.md#bluetooth-mesh-blob-cli)。

<a id="mesh-models-blob-cli-target-addr"></a>

##### 106.5.7.3.1 `mesh models blob cli target <Addr>`

> 为下一次 BLOB 传输添加目标节点。
>
> - `Addr`：目标节点 BLOB 传输服务端模型的单播地址。

<a id="mesh-models-blob-cli-caps-group-timeoutbase"></a>

##### 106.5.7.3.2 `mesh models blob cli caps [<Group> [<TimeoutBase>]]`

> 查询目标节点的传输能力。
>
> - `Group`：可选，与目标通信使用的组地址；省略时客户端逐个寻址各目标节点。
>
> - `TimeoutBase`：可选，等待目标响应的时间，以 10 秒为增量。

<a id="mesh-models-blob-cli-tx-id-size-blocksizelog-chunksize-group-mode-push-pull"></a>

##### 106.5.7.3.3 `mesh models blob cli tx <Id> <Size> <BlockSizeLog> <ChunkSize> [<Group> [<Mode(push, pull)>]]`

> 向目标节点执行 BLOB 传输。客户端向全部目标发送测试用 BLOB，完成后输出消息。注意，必须先在所有目标上用 `mesh models blob srv rx` 准备接收。
>
> - `Id`：64 位 BLOB 传输 ID。
>
> - `Size`：BLOB 大小，单位字节。
>
> - `BlockSizeLog`：块大小的对数表示，最终块大小为 `1 << block size log` 字节。
>
> - `ChunkSize`：Chunk 大小，单位字节。
>
> - `Group`：可选，与目标通信使用的组地址；省略或设为 0 时逐个寻址各目标。
>
> - `Mode`：BLOB 传输模式，必须是 `push`（推送模式，Push BLOB Transfer Mode）或 `pull`（拉取模式，Pull BLOB Transfer Mode）；省略时默认为 `push`。

<a id="mesh-models-blob-cli-tx-cancel"></a>

##### 106.5.7.3.4 `mesh models blob cli tx-cancel`

> 取消正在进行的 BLOB 传输。

<a id="mesh-models-blob-cli-tx-get-group"></a>

##### 106.5.7.3.5 `mesh models blob cli tx-get [Group]`

> 查询此前运行的 BLOB 传输的进度。可在当前没有执行 BLOB 传输时使用。
>
> - `Group`：可选，与目标通信使用的组地址；省略或设为 0 时逐个寻址各目标。

<a id="mesh-models-blob-cli-tx-suspend"></a>

##### 106.5.7.3.6 `mesh models blob cli tx-suspend`

> 暂停正在进行的 BLOB 传输。

<a id="mesh-models-blob-cli-tx-resume"></a>

##### 106.5.7.3.7 `mesh models blob cli tx-resume`

> 继续已暂停的 BLOB 传输。

<a id="mesh-models-blob-cli-instance-set-elemidx"></a>

##### 106.5.7.3.8 `mesh models blob cli instance-set <ElemIdx>`

> 为其他 BLOB 客户端命令选用指定元素上的客户端实例。
>
> - `ElemIdx`：所选 BLOB 客户端实例所在的元素。

<a id="mesh-models-blob-cli-instance-get-all"></a>

##### 106.5.7.3.9 `mesh models blob cli instance-get-all`

> 获取节点上全部 BLOB 客户端实例列表。

<a id="blob-transfer-server-model"></a>

#### 106.5.7.4 大对象传输服务端模型（BLOB Transfer Server model）

启用 [`CONFIG_BT_MESH_BLOB_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BLOB_SRV) 可加入 BLOB 传输服务端。模型能够接收任意 BLOB 数据，但 Mesh Shell 中的实现会丢弃收到的数据。 相关链接：[大对象传输服务端（BLOB Transfer Server）](P100_Mesh大对象传输服务端.md#bluetooth-mesh-blob-srv)。

<a id="mesh-models-blob-srv-rx-id-timeoutbase-10s-steps"></a>

##### 106.5.7.4.1 `mesh models blob srv rx <ID> [<TimeoutBase(10s steps)>]`

> 准备接收 BLOB 传输。
>
> - `ID`：要接收的 64 位 BLOB 传输 ID。
>
> - `TimeoutBase`：可选，等待客户端消息的额外时间，以 10 秒为增量。

<a id="mesh-models-blob-srv-rx-cancel"></a>

##### 106.5.7.4.2 `mesh models blob srv rx-cancel`

> 取消正在进行的 BLOB 传输。

<a id="mesh-models-blob-srv-instance-set-elemidx"></a>

##### 106.5.7.4.3 `mesh models blob srv instance-set <ElemIdx>`

> 为其他 BLOB 服务端命令选用指定元素上的服务端实例。
>
> - `ElemIdx`：所选 BLOB 服务端实例所在的元素。

<a id="mesh-models-blob-srv-instance-get-all"></a>

##### 106.5.7.4.4 `mesh models blob srv instance-get-all`

> 获取节点上全部 BLOB 服务端实例列表。

<a id="binary-large-object-blob-transfer-flash-stream"></a>

#### 106.5.7.5 二进制大对象传输 Flash 流（BLOB Transfer flash stream）

启用 [`CONFIG_BT_MESH_SHELL_BLOB_IO_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SHELL_BLOB_IO_FLASH)，可在 Shell 中配置 BLOB Flash 流。默认使用虚拟测试流（Dummy BLOB stream）；该选项允许指定实际使用的 Flash 区域。获取相关参数的方法见 [Flash 映射（Flash map）](../storage/P001_Flash分区映射.md#flash-map-api)。

<a id="mesh-models-blob-flash-stream-set-areaid-offset"></a>

##### 106.5.7.5.1 `mesh models blob flash-stream-set <AreaID> [<Offset>]`

> 将 BLOB 流设置到指定区域。
>
> - `AreaID`：读取／写入 BLOB 所用的 Flash 区域 ID。
>
> - `Offset`：可选，BLOB 在 Flash 区域内的存放偏移，以字节计。

<a id="mesh-models-blob-flash-stream-unset"></a>

##### 106.5.7.5.2 `mesh models blob flash-stream-unset`

> 将 BLOB 流切换回虚拟测试流。

<a id="firmware-update-client-model"></a>

#### 106.5.7.6 固件更新客户端模型（Firmware Update Client model）

同时启用 [`CONFIG_BT_MESH_BLOB_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BLOB_CLI) 和 [`CONFIG_BT_MESH_DFU_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_DFU_CLI) 可加入固件更新客户端。它向一组目标节点传输虚拟固件更新，演示固件更新分发器（Distributor）角色。

<a id="mesh-models-dfu-slot-add-size-fwid-metadata"></a>

##### 106.5.7.6.1 `mesh models dfu slot add <Size> <FwID> [<Metadata>]`

> 添加一个可作为 DFU 映像传输的虚拟映像槽。响应中打印所分配的槽索引，其他命令可据此引用。要更新槽，先用 `mesh models dfu slot del` 删除，再重新添加。
>
> - `Size`：DFU 映像槽大小，单位字节。
>
> - `FwID`：固件 ID，使用十六进制字符串。
>
> - `Metadata`：可选固件元数据，使用十六进制字符串。

<a id="mesh-models-dfu-slot-del-slotidx"></a>

##### 106.5.7.6.2 `mesh models dfu slot del <SlotIdx>`

> 删除指定索引的 DFU 映像槽。
>
> - `SlotIdx`：要删除的槽索引。

<a id="mesh-models-dfu-slot-get-slotidx"></a>

##### 106.5.7.6.3 `mesh models dfu slot get <SlotIdx>`

> 获取 DFU 映像槽的全部可用信息。
>
> - `SlotIdx`：要查询的槽索引。

<a id="mesh-models-dfu-cli-target-addr-imgidx"></a>

##### 106.5.7.6.4 `mesh models dfu cli target <Addr> <ImgIdx>`

> 添加目标节点。
>
> - `Addr`：目标节点单播地址。
>
> - `ImgIdx`：目标节点上要寻址的映像索引。

<a id="mesh-models-dfu-cli-target-state"></a>

##### 106.5.7.6.5 `mesh models dfu cli target-state`

> 检查已配置目标地址处设备的 DFU 目标状态。

<a id="mesh-models-dfu-cli-target-imgs-maxcount"></a>

##### 106.5.7.6.6 `mesh models dfu cli target-imgs [<MaxCount>]`

> 获取已配置目标地址处设备的 DFU 映像列表。
>
> - `MaxCount`：可选，最多返回的映像数量；省略时不限制。

<a id="mesh-models-dfu-cli-target-check-slotidx-targetimgidx"></a>

##### 106.5.7.6.7 `mesh models dfu cli target-check <SlotIdx> <TargetImgIdx>`

> 检查已配置目标地址处设备是否接受从给定本地映像槽更新到目标指定索引映像的 DFU 传输，并查询更新影响。
>
> - `SlotIdx`：要检查的本地 DFU 映像槽索引。
>
> - `TargetImgIdx`：要检查的目标节点 DFU 映像索引。

<a id="mesh-models-dfu-cli-send-slotidx-group"></a>

##### 106.5.7.6.8 `mesh models dfu cli send <SlotIdx> [<Group>]`

> 向所有已添加目标启动 DFU 传输。
>
> - `SlotIdx`：要发送的本地 DFU 映像槽索引。
>
> - `Group`：可选，与目标通信使用的组地址；省略时固件更新客户端逐个寻址各目标。

<a id="mesh-models-dfu-cli-cancel-addr"></a>

##### 106.5.7.6.9 `mesh models dfu cli cancel [<Addr>]`

> 在任意状态下取消指定目标或全部目标的 DFU 过程。提供目标地址时，客户端尝试取消该目标的过程；否则尝试取消所有目标上正在进行的 DFU 过程。
>
> - `Addr`：可选，要取消 DFU 的目标节点单播地址。

<a id="mesh-models-dfu-cli-apply"></a>

##### 106.5.7.6.10 `mesh models dfu cli apply`

> 在所有目标上应用最近一次 DFU 传输的映像。只能在传输完成后调用。

<a id="mesh-models-dfu-cli-confirm"></a>

##### 106.5.7.6.11 `mesh models dfu cli confirm`

> 确认最近一次 DFU 传输已在所有目标上成功应用。只能在传输完成并应用后调用。

<a id="mesh-models-dfu-cli-suspend"></a>

##### 106.5.7.6.12 `mesh models dfu cli suspend`

> 暂停正在进行的 DFU 传输。

<a id="mesh-models-dfu-cli-resume"></a>

##### 106.5.7.6.13 `mesh models dfu cli resume`

> 继续已暂停的 DFU 传输。

<a id="mesh-models-dfu-cli-progress"></a>

##### 106.5.7.6.14 `mesh models dfu cli progress`

> 检查当前传输进度。

<a id="mesh-models-dfu-cli-instance-set-elemidx"></a>

##### 106.5.7.6.15 `mesh models dfu cli instance-set <ElemIdx>`

> 为其他固件更新客户端命令选用指定元素上的客户端实例。
>
> - `ElemIdx`：所选固件更新客户端实例所在的元素。

<a id="mesh-models-dfu-cli-instance-get-all"></a>

##### 106.5.7.6.16 `mesh models dfu cli instance-get-all`

> 获取节点上全部固件更新客户端实例列表。

<a id="firmware-update-server-model"></a>

#### 106.5.7.7 固件更新服务端模型（Firmware Update Server model）

同时启用 [`CONFIG_BT_MESH_BLOB_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BLOB_SRV) 和 [`CONFIG_BT_MESH_DFU_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_DFU_SRV) 可加入固件更新服务端。它接受任意固件更新，以演示目标节点（Target）角色。Shell 中的服务端会丢弃传入的固件数据，其他行为则与正常固件更新目标节点相同。

<a id="mesh-models-dfu-srv-applied"></a>

##### 106.5.7.7.1 `mesh models dfu srv applied`

> 将最近一次 DFU 传输标记为已应用。只能在传输完成、且分发器已要求应用后调用。
>
> Shell 固件更新服务端不会实际应用收到的映像，因此可用此命令模拟已应用状态，通知分发器传输成功。

<a id="mesh-models-dfu-srv-progress"></a>

##### 106.5.7.7.2 `mesh models dfu srv progress`

> 检查当前传输进度。

<a id="mesh-models-dfu-srv-rx-cancel"></a>

##### 106.5.7.7.3 `mesh models dfu srv rx-cancel`

> 取消传入的 DFU 传输。

<a id="mesh-models-dfu-srv-instance-set-elemidx"></a>

##### 106.5.7.7.4 `mesh models dfu srv instance-set <ElemIdx>`

> 为其他固件更新服务端命令选用指定元素上的服务端实例。
>
> - `ElemIdx`：所选固件更新服务端实例所在的元素。

<a id="mesh-models-dfu-srv-instance-get-all"></a>

##### 106.5.7.7.5 `mesh models dfu srv instance-get-all`

> 获取节点上全部固件更新服务端实例列表。

<a id="firmware-distribution-server-model"></a>

<a id="bluetooth-mesh-shell-dfd-server"></a>

#### 106.5.7.8 固件分发服务端模型（Firmware Distribution Server model）

启用 [`CONFIG_BT_MESH_DFD_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_DFD_SRV) 可加入固件分发服务端命令。这些命令对应固件分发客户端模型向服务端发送的消息。使用前，应用必须实例化固件分发服务端。

<a id="mesh-models-dfd-receivers-add-addr-fwidx-addr-fwidx"></a>

##### 106.5.7.8.1 `mesh models dfd receivers-add <Addr>,<FwIdx>[;<Addr>,<FwIdx>]...`

> 向固件分发服务端添加接收者。每项使用逗号分隔的 addr,fw_idx 对，各项之间用分号分隔，例如 `0x0001,0;0x0002,0;0x0004,1`，列表中不要使用空格。重复调用会持续追加接收者，直到执行 `mesh models dfd receivers-delete-all`。
>
> - `Addr`：接收节点地址。
>
> - `FwIdx`：要发送给 `Addr` 的固件槽索引。

> 译注——两个索引不能混用：原文把 `FwIdx` 称作要发送的固件槽索引。本次[官方 dfd.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/shell/dfd.c)将接收者列表第二项解析为 `img_idx`，交给 `bt_mesh_dfd_srv_receiver_add()`；它对应目标节点要更新的映像索引。分发器上待发送映像的本地槽则由后面的 `SlotIdx` 选择，见[DFU 分发过程](P102_Mesh设备固件更新.md#populating-the-distributor-s-receivers-list)。本仓库相对[实现](../../../subsys/bluetooth/mesh/shell/dfd.c)可用于对照。

<a id="mesh-models-dfd-receivers-delete-all"></a>

##### 106.5.7.8.2 `mesh models dfd receivers-delete-all`

> 从服务端删除全部接收者。

<a id="mesh-models-dfd-receivers-get-first-count"></a>

##### 106.5.7.8.3 `mesh models dfd receivers-get <First> <Count>`

> 获取固件接收者信息列表。
>
> - `First`：接收者列表中首个查询项的索引。
>
> - `Count`：要查询的接收者数量。

<a id="mesh-models-dfd-capabilities-get"></a>

##### 106.5.7.8.4 `mesh models dfd capabilities-get`

> 获取服务端能力。

<a id="mesh-models-dfd-get"></a>

##### 106.5.7.8.5 `mesh models dfd get`

> 获取当前分发状态、阶段和传输参数。

<a id="mesh-models-dfd-start-appkeyidx-slotidx-group-policyapply-ttl-timeoutbase-xfermode"></a>

##### 106.5.7.8.6 `mesh models dfd start <AppKeyIdx> <SlotIdx> [<Group> [<PolicyApply> [<TTL> [<TimeoutBase> [<XferMode>]]]]]`

> 开始固件分发。
>
> - `AppKeyIdx`：发送使用的应用索引。分发器和目标节点上的固件更新模型、BLOB 传输模型都应绑定同一个应用密钥。
>
> - `SlotIdx`：要发送的本地映像槽索引。
>
> - `Group`：可选，与目标通信使用的组地址；省略时服务端逐个寻址各目标。如果修改后续参数时仍希望逐个寻址，将此参数设为 0。
>
> - `PolicyApply`：可选的更新策略字段。设为 `true` 时，服务端在传输完成后立即要求应用映像。
>
> - `TTL`：可选，发送时使用的 TTL；默认使用已配置的默认 TTL。
>
> - `TimeoutBase`：可选，用于计算分发过程中超时值的额外参数，以 10 秒为增量，默认为 0。`timeout_base` 的计算方式见[传输超时（Transfer timeout）](P098_Mesh大对象传输.md#bluetooth-mesh-blob-timeout)。
>
> - `XferMode`：可选 BLOB 传输模式；1 为推送（Push BLOB Transfer Mode），2 为拉取（Pull BLOB Transfer Mode）。默认推送模式。

<a id="mesh-models-dfd-suspend"></a>

##### 106.5.7.8.7 `mesh models dfd suspend`

> 暂停正在进行的分发。

<a id="mesh-models-dfd-cancel"></a>

##### 106.5.7.8.8 `mesh models dfd cancel`

> 取消正在进行的分发。

<a id="mesh-models-dfd-apply"></a>

##### 106.5.7.8.9 `mesh models dfd apply`

> 应用已分发的固件。

<a id="mesh-models-dfd-fw-get-fwid"></a>

##### 106.5.7.8.10 `mesh models dfd fw-get <FwID>`

> 获取已上传到服务端的固件映像信息。
>
> - `FwID`：要查询的映像固件 ID。

<a id="mesh-models-dfd-fw-get-by-idx-idx"></a>

##### 106.5.7.8.11 `mesh models dfd fw-get-by-idx <Idx>`

> 获取服务端指定槽内已上传映像的信息。
>
> - `Idx`：要查询映像的槽索引。

<a id="mesh-models-dfd-fw-delete-fwid"></a>

##### 106.5.7.8.12 `mesh models dfd fw-delete <FwID>`

> 从服务端删除一个固件映像。
>
> - `FwID`：要删除的映像固件 ID。

<a id="mesh-models-dfd-fw-delete-all"></a>

##### 106.5.7.8.13 `mesh models dfd fw-delete-all`

> 从服务端删除全部固件映像。

<a id="mesh-models-dfd-instance-set-elemidx"></a>

##### 106.5.7.8.14 `mesh models dfd instance-set <ElemIdx>`

> 为其他固件分发服务端命令选用指定元素上的服务端实例。
>
> - `ElemIdx`：所选固件分发服务端实例所在的元素。

<a id="mesh-models-dfd-instance-get-all"></a>

##### 106.5.7.8.15 `mesh models dfd instance-get-all`

> 获取节点上全部固件分发服务端实例列表。

<a id="dfu-metadata"></a>

<a id="bluetooth-mesh-shell-dfu-metadata"></a>

#### 106.5.7.9 DFU 元数据（DFU metadata）

DFU 元数据命令可生成元数据，供目标节点在接受固件前检查。通过 [`CONFIG_BT_MESH_SHELL_DFU_METADATA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SHELL_DFU_METADATA) 启用。

<a id="mesh-models-dfu-metadata-comp-clear"></a>

##### 106.5.7.9.1 `mesh models dfu metadata comp-clear`

> 清除为目标节点保存的组成数据。

<a id="mesh-models-dfu-metadata-comp-add-cid-productid-vendorid-crpl-features"></a>

##### 106.5.7.9.2 `mesh models dfu metadata comp-add <CID> <ProductID> <VendorID> <Crpl> <Features>`

> 创建组成数据第 0 页的页头。
>
> - `CID`：Bluetooth SIG 分配的公司标识。
>
> - `ProductID`：厂商分配的产品标识。
>
> - `VendorID`：厂商分配的版本标识。
>
> - `Crpl`：重放保护列表大小。
>
> - `Features`：节点支持的功能，以位字段表示：
>
>   > - `0`：中继（Relay）。
> >
> > - `1`：代理（Proxy）。
> >
> > - `2`：Friend。
> >
> > - `3`：低功耗（Low Power）。

> 译注——字段名：原命令将参数拼作 `VendorID`，正文却明确说明它是版本标识（Version identifier），不是公司标识。组成数据中的公司标识已由 `CID` 单独传入，复制命令时保留参数顺序。

<a id="mesh-models-dfu-metadata-comp-elem-add-loc-nums-numv-sigmid-vndcid-vndmid"></a>

##### 106.5.7.9.3 `mesh models dfu metadata comp-elem-add <Loc> <NumS> <NumV> {<SigMID>|<VndCID> <VndMID>}...`

> 添加目标节点的元素描述。
>
> - `Loc`：元素位置。
>
> - `NumS`：该元素上实例化的 SIG 模型数量。
>
> - `NumV`：该元素上实例化的厂商模型数量。
>
> - `SigMID`：SIG 模型 ID。
>
> - `VndCID`：厂商模型公司标识。
>
> - `VndMID`：厂商模型标识。

<a id="mesh-models-dfu-metadata-comp-hash-get-key-16-hex"></a>

##### 106.5.7.9.4 `mesh models dfu metadata comp-hash-get [<Key(16 hex)>]`

> 对已保存的组成数据生成散列值（Hash），用于元数据。
>
> - `Key`：可选，用于生成散列的 128 位密钥。十六进制字符串不足 16 字节时填入数组的 N 个最高有效字节，其余补零。

<a id="mesh-models-dfu-metadata-encode-major-minor-rev-buildnum-size-coretype-hash-elems-userdata"></a>

##### 106.5.7.9.5 `mesh models dfu metadata encode <Major> <Minor> <Rev> <BuildNum> <Size> <CoreType> <Hash> <Elems> [<UserData>]`

> 编码 DFU 元数据。
>
> - `Major`：固件主版本号。
>
> - `Minor`：固件次版本号。
>
> - `Rev`：固件修订号。
>
> - `BuildNum`：构建号。
>
> - `Size`：已签名 bin 文件的大小。
>
> - `CoreType`：新固件的内核类型：
>
>   > - `1`：应用核（Application core）。
> >
> > - `2`：网络核（Network core）。
> >
> > - `4`：应用专用 BLOB（Application-specific BLOB）。
>
> - `Hash`：通过 `mesh models dfu metadata comp-hash-get` 生成的组成数据散列值。
>
> - `Elems`：新固件的元素数量。
>
> - `UserData`：随元数据提供的用户数据。

<a id="segmentation-and-reassembly-sar-configuration-client"></a>

#### 106.5.7.10 分段与重组配置客户端（Segmentation and Reassembly Configuration Client，SAR）

SAR 配置客户端是可选 Mesh 模型，通过 [`CONFIG_BT_MESH_SAR_CFG_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SAR_CFG_CLI) 启用。它用于配置支持 SAR 配置服务端的节点的下层传输层行为。

<a id="mesh-models-sar-tx-get"></a>

##### 106.5.7.10.1 `mesh models sar tx-get`

> 发送 SAR 配置发送端获取（SAR Configuration Transmitter Get）消息。

<a id="mesh-models-sar-tx-set-segintstep-uniretranscnt-uniretranswithoutprogcnt-uniretransintstep-uniretransintinc-multiretranscnt-multiretransint"></a>

##### 106.5.7.10.2 `mesh models sar tx-set <SegIntStep> <UniRetransCnt> <UniRetransWithoutProgCnt> <UniRetransIntStep> <UniRetransIntInc> <MultiRetransCnt> <MultiRetransInt>`

> 发送 SAR 配置发送端设置（SAR Configuration Transmitter Set）消息。
>
> - `SegIntStep`：SAR 分段间隔步长（Segment Interval Step）状态。
>
> - `UniRetransCnt`：SAR 单播重传次数（Unicast Retransmissions Count）状态。
>
> - `UniRetransWithoutProgCnt`：SAR 无进展单播重传次数（Unicast Retransmissions Without Progress Count）状态。
>
> - `UniRetransIntStep`：SAR 单播重传间隔步长（Unicast Retransmissions Interval Step）状态。
>
> - `UniRetransIntInc`：SAR 单播重传间隔增量（Unicast Retransmissions Interval Increment）状态。
>
> - `MultiRetransCnt`：SAR 多播重传次数（Multicast Retransmissions Count）状态。
>
> - `MultiRetransInt`：SAR 多播重传间隔（Multicast Retransmissions Interval）状态。

<a id="mesh-models-sar-rx-get"></a>

##### 106.5.7.10.3 `mesh models sar rx-get`

> 发送 SAR 配置接收端获取（SAR Configuration Receiver Get）消息。

<a id="mesh-models-sar-rx-set-segthresh-ackdelayinc-discardtimeout-rxsegintstep-ackretranscount"></a>

##### 106.5.7.10.4 `mesh models sar rx-set <SegThresh> <AckDelayInc> <DiscardTimeout> <RxSegIntStep> <AckRetransCount>`

> 发送 SAR 配置接收端设置（SAR Configuration Receiver Set）消息。
>
> - `SegThresh`：SAR 分段数阈值（Segments Threshold）状态。
>
> - `AckDelayInc`：SAR 确认延迟增量（Acknowledgment Delay Increment）状态。
>
> - `DiscardTimeout`：SAR 丢弃超时（Discard Timeout）状态。
>
> - `RxSegIntStep`：SAR 接收端分段间隔步长（Receiver Segment Interval Step）状态。
>
> - `AckRetransCount`：SAR 确认重传次数（Acknowledgment Retransmissions Count）状态。

<a id="private-beacon-client"></a>

#### 106.5.7.11 私有信标客户端（Private Beacon Client）

私有信标客户端模型是可选子系统，通过 [`CONFIG_BT_MESH_PRIV_BEACON_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PRIV_BEACON_CLI) 启用。

<a id="mesh-models-prb-priv-beacon-get"></a>

##### 106.5.7.11.1 `mesh models prb priv-beacon-get`

> 获取目标的私有信标状态，可能值如下：
>
> > - `0x00`：节点不广播私有信标。
> >
> > - `0x01`：节点广播私有信标。

<a id="mesh-models-prb-priv-beacon-set-val-off-on-randint-10s-steps"></a>

##### 106.5.7.11.2 `mesh models prb priv-beacon-set <Val(off, on)> <RandInt(10s steps)>`

> 设置目标的私有信标状态。
>
> - `Val`：控制私有信标状态。
>
> - `RandInt`：随机数刷新间隔，以 10 秒为步长；0 表示保留当前值。

<a id="mesh-models-prb-priv-gatt-proxy-get"></a>

##### 106.5.7.11.3 `mesh models prb priv-gatt-proxy-get`

> 获取目标的私有 GATT 代理（Private GATT Proxy）状态，可能值如下：
>
> > - `0x00`：支持私有代理，但未启用。
> >
> > - `0x01`：已启用私有代理。
> >
> > - `0x02`：不支持私有代理。

<a id="mesh-models-prb-priv-gatt-proxy-set-val-off-on"></a>

##### 106.5.7.11.4 `mesh models prb priv-gatt-proxy-set <Val(off, on)>`

> 设置目标的私有 GATT 代理状态。
>
> - `Val`：新的私有 GATT 代理值：
>
>   > - `0x00`：禁用私有代理功能。
> >
> > - `0x01`：启用私有代理功能。

<a id="mesh-models-prb-priv-node-id-get-netkeyidx"></a>

##### 106.5.7.11.5 `mesh models prb priv-node-id-get <NetKeyIdx>`

> 获取目标的私有节点身份（Private Node Identity）状态，可能值如下：
>
> > - `0x00`：节点不广播私有节点身份。
> >
> > - `0x01`：节点广播私有节点身份。
> >
> > - `0x02`：节点不支持广播私有节点身份。
>
> - `NetKeyIdx`：要查询私有节点身份状态的网络索引。

<a id="mesh-models-prb-priv-node-id-set-netkeyidx-state"></a>

##### 106.5.7.11.6 `mesh models prb priv-node-id-set <NetKeyIdx> <State>`

> 设置目标的私有节点身份状态。
>
> - `NetKeyIdx`：要设置私有节点身份状态的网络索引。
>
> - `State`：新的私有节点身份值：
>
>   > - `0x00`：停止广播私有节点身份。
> >
> > - `0x01`：开始广播私有节点身份。

<a id="opcodes-aggregator-client"></a>

#### 106.5.7.12 操作码聚合器客户端（Opcodes Aggregator Client）

操作码聚合器客户端是可选模型，通过 [`CONFIG_BT_MESH_OP_AGG_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OP_AGG_CLI) 启用。它可向支持操作码聚合器服务端的节点发送一系列访问层消息。

<a id="mesh-models-opagg-seq-start-elemaddr"></a>

##### 106.5.7.12.1 `mesh models opagg seq-start <ElemAddr>`

> 开始构造操作码聚合器序列（Opcodes Aggregator Sequence）消息。该命令初始化消息聚合上下文，并将后续 Shell 命令的目标地址设为 `elem_addr`。
>
> - `ElemAddr`：处理所聚合操作码的元素地址。

<a id="mesh-models-opagg-seq-send"></a>

##### 106.5.7.12.2 `mesh models opagg seq-send`

> 发送操作码聚合器序列消息。该命令结束构造过程，将聚合的序列消息发送给目标节点，并清除上下文。

<a id="mesh-models-opagg-seq-abort"></a>

##### 106.5.7.12.3 `mesh models opagg seq-abort`

> 放弃操作码聚合器序列消息，清除客户端上下文。

<a id="remote-provisioning-client"></a>

#### 106.5.7.13 远程配网客户端（Remote Provisioning Client）

远程配网客户端是可选模型，通过 [`CONFIG_BT_MESH_RPR_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPR_CLI) 启用。它借助远程配网服务端，将设备远程加入 Mesh 网络。

该 Shell 模块可触发网络设备上的远程配网客户端与服务端交互。

<a id="mesh-models-rpr-scan-timeout-s-uuid-1-16-hex"></a>

##### 106.5.7.13.1 `mesh models rpr scan <Timeout(s)> [<UUID(1-16 hex)>]`

> 开始扫描未配网设备。
>
> - `Timeout`：扫描超时，单位秒，至少为 1 秒。
>
> - `UUID`：要扫描的设备 UUID。不足 16 字节的十六进制字符串填入数组的 N 个最高有效字节，其余补零；省略时报告所有设备。

<a id="mesh-models-rpr-scan-ext-timeout-s-uuid-1-16-hex-adtype"></a>

##### 106.5.7.13.2 `mesh models rpr scan-ext <Timeout(s)> <UUID(1-16 hex)> [<ADType> ... ]`

> 开始未配网设备的扩展扫描（Extended scanning）。
>
> - `Timeout`：扫描超时，单位秒，有效范围为 [`BT_MESH_RPR_EXT_SCAN_TIME_MIN`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga2b7e2636da150f5c5cb4e3bdee13c745) 至 [`BT_MESH_RPR_EXT_SCAN_TIME_MAX`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr.html#ga2a5241b2e87fec227740dd4f2de3a68a)。
>
> - `UUID`：要扩展扫描的设备 UUID。不足 16 字节的十六进制字符串填入数组的 N 个最高有效字节，其余补零。
>
> - `ADType`：扫描报告中要包含的广播数据类型（AD type）列表，必须有 1 至 [`CONFIG_BT_MESH_RPR_AD_TYPES_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPR_AD_TYPES_MAX) 项。

<a id="mesh-models-rpr-scan-srv-adtype"></a>

##### 106.5.7.13.3 `mesh models rpr scan-srv [<ADType> ... ]`

> 开始针对远程配网服务端自身的扩展扫描。
>
> - `ADType`：扫描报告中要包含的广播数据类型（AD type）列表，必须有 1 至 [`CONFIG_BT_MESH_RPR_AD_TYPES_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPR_AD_TYPES_MAX) 项。

<a id="mesh-models-rpr-scan-caps"></a>

##### 106.5.7.13.4 `mesh models rpr scan-caps`

> 获取远程配网服务端的扫描能力。

<a id="mesh-models-rpr-scan-get"></a>

##### 106.5.7.13.5 `mesh models rpr scan-get`

> 获取远程配网服务端当前扫描状态。

<a id="mesh-models-rpr-scan-stop"></a>

##### 106.5.7.13.6 `mesh models rpr scan-stop`

> 停止服务端上正在进行的扫描。

<a id="mesh-models-rpr-link-get"></a>

##### 106.5.7.13.7 `mesh models rpr link-get`

> 获取远程配网服务端当前链路状态。

<a id="mesh-models-rpr-link-close"></a>

##### 106.5.7.13.8 `mesh models rpr link-close`

> 关闭远程配网服务端上已打开的链路。

<a id="mesh-models-rpr-provision-remote-uuid-1-16-hex-netkeyidx-addr"></a>

##### 106.5.7.13.9 `mesh models rpr provision-remote <UUID(1-16 hex)> <NetKeyIdx> <Addr>`

> 使用 PB-Remote 配网承载为 Mesh 节点配网。
>
> - `UUID`：未配网节点的 UUID。不足 16 字节的十六进制字符串填入数组的 N 个最高有效字节，其余补零。
>
> - `NetKeyIdx`：提供给未配网节点的网络密钥索引。
>
> - `Addr`：分配给远程设备的地址；`addr` 为 0 时选择最低可用地址。

<a id="mesh-models-rpr-reprovision-remote-addr-compchanged-false-true"></a>

##### 106.5.7.13.10 `mesh models rpr reprovision-remote <Addr> [<CompChanged(false, true)>]`

> 使用 PB-Remote 配网承载为 Mesh 节点重新配网。
>
> - `Addr`：分配给远程设备的地址；`addr` 为 0 时选择最低可用地址。
>
> - `CompChanged`：目标节点已指示其组成数据发生变化，默认为 false。

<a id="mesh-models-rpr-instance-set-elemidx"></a>

##### 106.5.7.13.11 `mesh models rpr instance-set <ElemIdx>`

> 为其他远程配网客户端命令选用指定元素上的客户端实例。
>
> - `ElemIdx`：所选远程配网客户端实例所在的元素。

<a id="mesh-models-rpr-instance-get-all"></a>

##### 106.5.7.13.12 `mesh models rpr instance-get-all`

> 获取节点上全部远程配网客户端实例列表。

<a id="large-composition-data-client"></a>

#### 106.5.7.14 大型组成数据客户端（Large Composition Data Client）

大型组成数据客户端是可选模型，通过 [`CONFIG_BT_MESH_LARGE_COMP_DATA_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LARGE_COMP_DATA_CLI) 启用。它可读取无法装入一条 Config Composition Data Status 消息的组成数据页，以及模型实例的元数据。

<a id="mesh-models-lcd-large-comp-data-get-page-offset"></a>

##### 106.5.7.14.1 `mesh models lcd large-comp-data-get <Page> <Offset>`

> 发送大型组成数据获取（Large Composition Data Get）消息，查询节点组成数据状态的一部分。
>
> - `Page`：组成数据页码。
>
> - `Offset`：页内偏移。

<a id="mesh-models-lcd-models-metadata-get-page-offset"></a>

##### 106.5.7.14.2 `mesh models lcd models-metadata-get <Page> <Offset>`

> 发送模型元数据获取（Models Metadata Get）消息，查询模型元数据某一页的一部分。
>
> - `Page`：模型元数据页码。
>
> - `Offset`：页内偏移。

<a id="bridge-configuration-client"></a>

#### 106.5.7.15 桥接配置客户端（Bridge Configuration Client）

桥接配置客户端是可选模型，通过 [`CONFIG_BT_MESH_BRG_CFG_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_BRG_CFG_CLI) 启用，用于配置 Mesh 节点的子网桥接功能。

<a id="mesh-models-brg-get"></a>

##### 106.5.7.15.1 `mesh models brg get`

> 获取当前子网桥接（Subnet Bridge）状态。

<a id="mesh-models-brg-set-state-disable-enable"></a>

##### 106.5.7.15.2 `mesh models brg set <State(disable, enable)>`

> 设置子网桥接状态。
>
> - `State`：禁用或启用子网桥接。

<a id="mesh-models-brg-table-size-get"></a>

##### 106.5.7.15.3 `mesh models brg table-size-get`

> 获取当前桥接表（Bridging Table）大小。

<a id="mesh-models-brg-table-add-directions-netidx1-netidx2-addr1-addr2"></a>

##### 106.5.7.15.4 `mesh models brg table-add <Directions> <NetIdx1> <NetIdx2> <Addr1> <Addr2>`

> 向桥接表添加条目。
>
> - `Directions`：允许的桥接流量方向，有效值如下：
>
>   > - `0x01`：只允许源地址为 `Addr1`、目标地址为 `Addr2` 的消息通过桥接。
> >
> > - `0x02`：允许双向桥接。
>
> - `NetIdx1`：第一个子网的网络密钥索引。
>
> - `NetIdx2`：第二个子网的网络密钥索引。
>
> - `Addr1`：第一个子网中的节点地址。
>
> - `Addr2`：第二个子网中的节点地址。

<a id="mesh-models-brg-table-remove-netidx1-netidx2-addr1-addr2"></a>

##### 106.5.7.15.5 `mesh models brg table-remove <NetIdx1> <NetIdx2> <Addr1> <Addr2>`

> 从桥接表移除条目。
>
> - `NetIdx1`：第一个子网的网络密钥索引。
>
> - `NetIdx2`：第二个子网的网络密钥索引。
>
> - `Addr1`：第一个子网中的节点地址。
>
> - `Addr2`：第二个子网中的节点地址。

<a id="mesh-models-brg-subnets-get-filter-netidx-startidx"></a>

##### 106.5.7.15.6 `mesh models brg subnets-get <Filter> <NetIdx> <StartIdx>`

> 获取从桥接表提取并经过过滤的网络密钥索引对集合。
>
> - `Filter`：报告桥接表中的网络密钥索引对时使用的过滤条件，允许值如下：
>
>   > - `0x00`：报告全部索引对。
> >
> > - `0x01`：报告第一个子网的网络密钥索引匹配 `NetIdx` 的索引对。
> >
> > - `0x02`：报告第二个子网的网络密钥索引匹配 `NetIdx` 的索引对。
> >
> > - `0x03`：报告任一网络密钥索引匹配 `NetIdx` 的索引对。
>
> - `NetIdx`：任一子网的网络密钥索引。
>
> - `StartIdx`：读取起始偏移，以网络密钥索引对为单位。

<a id="mesh-models-brg-table-get-netidx1-netidx2-startidx"></a>

##### 106.5.7.15.7 `mesh models brg table-get <NetIdx1> <NetIdx2> <StartIdx>`

> 获取桥接表条目的地址和允许流量方向列表。
>
> - `NetIdx1`：第一个子网的网络密钥索引。
>
> - `NetIdx2`：第二个子网的网络密钥索引。
>
> - `StartIdx`：读取起始偏移，以桥接表状态条目为单位。

<a id="configuration-database"></a>

### 106.5.8 [配置数据库（Configuration database）](#id11)

配置数据库是可选子系统，通过 [`CONFIG_BT_MESH_CDB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_CDB) 启用。它仅用于配网器设备，允许保存 Mesh 网络的全部信息。为避免冲突，网络中应仅有一个节点启用 CDB。该节点是配置器（Configurator），负责添加和配置新节点。

<a id="mesh-cdb-create-netkey-1-16-hex"></a>

#### 106.5.8.1 `mesh cdb create [NetKey(1-16 hex)]`

> 创建配置数据库。
>
> - `NetKey`：可选，主网络密钥（NetKeyIndex=0）的值。不足 16 字节的十六进制字符串填入数组的 N 个最高有效字节，其余补零；省略时使用默认密钥值。

<a id="mesh-cdb-clear"></a>

#### 106.5.8.2 `mesh cdb clear`

> 清空配置数据库中的全部数据。

> 译注——CDB 与节点网络状态：清空或删除 CDB 记录是修改配网器保存的数据库，不会自动让远端设备解除配网，也不等于远端已擦除密钥。后文节点删除步骤仍要求先处理目标节点状态。

<a id="mesh-cdb-show"></a>

#### 106.5.8.3 `mesh cdb show`

> 显示配置数据库中的全部数据。

<a id="mesh-cdb-node-add-uuid-1-16-hex-addr-elemcnt-netkeyidx-devkey-1-16-hex"></a>

#### 106.5.8.4 `mesh cdb node-add <UUID(1-16 hex)> <Addr> <ElemCnt> <NetKeyIdx> [DevKey(1-16 hex)]`

> 手动将 Mesh 节点加入配置数据库。注意，启用并创建 CDB 后，使用 `mesh provision` 和 `mesh provision-adv` 配网的设备会自动加入数据库。
>
> - `UUID`：节点的 128 位十六进制 UUID。不足 16 字节时填入数组的 N 个最高有效字节，其余补零。
>
> - `Addr`：节点单播地址；0 表示自动选择最低可用地址。
>
> - `ElemCnt`：节点的元素数量。
>
> - `NetKeyIdx`：节点配网时使用的网络密钥。
>
> - `DevKey`：可选，设备的 128 位设备密钥。不足 16 字节的十六进制字符串填入数组的 N 个最高有效字节，其余补零；省略时生成随机值。

> 译注——旧命令名称：原段的 `mesh provision`、`mesh provision-adv` 与本页前面列出的 `mesh prov local`、`mesh prov remote-adv`／`remote-gatt` 不一致。本次官方 Shell 注册表使用后一种分组；这里保留原句供对照，实际按设备提供的 `mesh prov` 帮助执行。

<a id="mesh-cdb-node-del-addr"></a>

#### 106.5.8.5 `mesh cdb node-del <Addr>`

> 从 CDB 删除 Mesh 节点。为避免意外行为及不受控的网络访问，条件允许时应先通过 `mesh reset` 重置节点，再从数据库删除。
>
> - `Addr`：要删除的节点地址。

> 译注——重置目标：原文 `mesh reset` 是旧名称。本次[官方配置客户端实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/shell/cfg.c)注册的是 `mesh models cfg reset`，按当前目标上下文操作；`mesh reset-local` 则重置本地设备并可能清除本地 CDB，两者不能互换。执行前应核对设备版本、目标地址及所用设备密钥。相对[实现](../../../subsys/bluetooth/mesh/shell/cfg.c)可供跟踪。

<a id="mesh-cdb-subnet-add-netkeyidx-netkey-1-16-hex"></a>

#### 106.5.8.6 `mesh cdb subnet-add <NetKeyIdx> [<NetKey(1-16 hex)>]`

> 向 CDB 添加网络密钥，之后可将其提供给网络节点。注意，加入 CDB 不会自动加入本地节点的已知网络密钥列表。
>
> - `NetKeyIdx`：要添加的网络密钥索引。
>
> - `NetKey`：可选，128 位网络密钥。不足 16 字节的十六进制字符串填入数组的 N 个最高有效字节，其余补零；省略时生成随机值。

<a id="mesh-cdb-subnet-del-netkeyidx"></a>

#### 106.5.8.7 `mesh cdb subnet-del <NetKeyIdx>`

> 从 CDB 删除网络密钥。
>
> - `NetKeyIdx`：要删除的网络密钥索引。

<a id="mesh-cdb-app-key-add-netkeyidx-appkeyidx-appkey-1-16-hex"></a>

#### 106.5.8.8 `mesh cdb app-key-add <NetKeyIdx> <AppKeyIdx> [<AppKey(1-16 hex)>]`

> 向 CDB 添加应用密钥，之后可将其提供给网络节点。注意，加入 CDB 不会自动加入本地节点的已知应用密钥列表。
>
> - `NetKeyIdx`：应用密钥绑定的网络密钥索引。
>
> - `AppKeyIdx`：要添加的应用密钥索引。
>
> - `AppKey`：可选，128 位应用密钥。不足 16 字节的十六进制字符串填入数组的 N 个最高有效字节，其余补零；省略时生成随机值。

<a id="mesh-cdb-app-key-del-appkeyidx"></a>

#### 106.5.8.9 `mesh cdb app-key-del <AppKeyIdx>`

> 从 CDB 删除应用密钥。
>
> - `AppKeyIdx`：要删除的应用密钥索引。

<a id="on-demand-private-gatt-proxy-client"></a>

#### 106.5.8.10 按需私有 GATT 代理客户端（On-Demand Private GATT Proxy Client）

按需私有 GATT 代理客户端是可选子系统，通过 [`CONFIG_BT_MESH_OD_PRIV_PROXY_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_OD_PRIV_PROXY_CLI) 启用。

<a id="mesh-models-od-priv-proxy-od-priv-gatt-proxy-dur-s"></a>

#### 106.5.8.11 `mesh models od\_priv\_proxy od-priv-gatt-proxy [Dur(s)]`

> 设置当前目标的按需私有 GATT 代理状态，或读取该状态值。
>
> - `Dur`：提供时将状态设为给定秒数；否则读取当前值。

<a id="solicitation-pdu-rpl-client"></a>

#### 106.5.8.12 请求 PDU 重放保护列表客户端（Solicitation PDU RPL Client）

请求 PDU RPL 客户端是可选子系统，通过 [`CONFIG_BT_MESH_SOL_PDU_RPL_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SOL_PDU_RPL_CLI) 启用。

<a id="mesh-models-sol-pdu-rpl-sol-pdu-rpl-clear-rngstart-ackd-rnglen"></a>

#### 106.5.8.13 `mesh models sol\_pdu\_rpl sol-pdu-rpl-clear <RngStart> <Ackd> [RngLen]`

> 清除当前目标请求重放保护列表（Solicitation Replay Protection List，SRPL）中指定请求源（Solicitation Source，SSRC）地址范围的条目。
>
> - `RngStart`：SSRC 范围的起始地址。
>
> - `Ackd`：决定发送需要确认还是无需确认的消息。
>
> - `RngLen`：要从请求 RPL 清除的 SSRC 地址范围长度。此参数可选，省略时仅清除单个 SSRC 地址。

<a id="statistic"></a>

### 106.5.9 [统计（Statistic）](#id12)

统计是可选 Mesh 模块，通过 [`CONFIG_BT_MESH_STATISTIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_STATISTIC) 启用。

<a id="mesh-stat-adv-get"></a>

#### 106.5.9.1 `mesh stat adv\_get`

> 获取帧统计，打印接收帧数量，以及计划发送和成功发送的尝试次数。

<a id="mesh-stat-adv-clear"></a>

#### 106.5.9.2 `mesh stat adv\_clear`

> 清除此前收集的帧统计。

<a id="mesh-stat-lpn-get"></a>

#### 106.5.9.3 `mesh stat lpn\_get`

> 获取测量的 LPN 友谊时序参数。命令打印根据轮询周期内时间戳计算的接收延迟（ReceiveDelay）和接收窗口（ReceiveWindow）。需要 [`CONFIG_BT_MESH_LOW_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LOW_POWER)。

<a id="mesh-stat-lpn-clear"></a>

#### 106.5.9.4 `mesh stat lpn\_clear`

> 清除此前收集的 LPN 时序统计，需要 [`CONFIG_BT_MESH_LOW_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_LOW_POWER)。

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/shell.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/shell.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/shell.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh固件分发服务端](P105_Mesh固件分发服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P105_Mesh固件分发服务端.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->

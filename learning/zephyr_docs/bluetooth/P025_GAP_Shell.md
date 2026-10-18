---
id: learning.zephyr-docs.bluetooth.page-25
title: GAP_Shell
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/host/gap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-gap-shell"></a>

# 第25章\_GAP\_Shell

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/shell/host/gap.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——使用前提：以下命令在启用了对应蓝牙功能的目标固件Zephyr Shell中执行，初始化与接入方式见[蓝牙Shell](P007_蓝牙Shell.md)。代码中的 `uart:~$` 是提示符，其后输出是原文预期结果；输入命令时不复制提示符和日志。若命令不可用或初始化失败，应先检查目标配置、控制器能力及当前版本帮助，再继续连接或传输步骤。本批仅翻译与核对文档，未连接设备或执行这些命令。

通用访问配置文件（Generic Access Profile，GAP）Shell是蓝牙的主要命令行接口，负责连接管理、扫描、广播等操作。

<a id="identities"></a>

## 25.1\_身份（Identities）

身份（Identity）是Zephyr主机（Host）的概念，可使一个物理设备表现为多个逻辑蓝牙设备。

Shell允许创建多个身份，上限由 [`CONFIG_BT_ID_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ID_MAX) 设置。用 `bt id-create` 创建新身份，再用 `bt id-select <id>` 按标识选择它。原文用 `id-show` 表示列出所有可用身份的子命令。

> 译注——命令前缀：[官方Shell实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/host/shell/bt.c)把 `id-show` 注册在 `bt` 下；在根提示符处应输入完整命令 `bt id-show`。

<a id="scan-for-devices"></a>

## 25.2\_扫描设备（Scan for devices）

用 `bt scan on` 开始扫描。视周围环境而定，Shell可能打印很多行。执行 `bt scan off` 停止扫描，输出滚动也应停止。以下是原文的预期示例：

```text
uart:~$ bt scan on
Bluetooth active scan enabled
[DEVICE]: R:CB:01:1A:2D:6E:AE, AD evt type 0, RSSI -78  C:1 S:1 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: R:20:C2:EE:59:85:5B, AD evt type 3, RSSI -62  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: R:E3:72:76:87:2F:E8, AD evt type 3, RSSI -74  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: R:1E:19:25:8A:CB:84, AD evt type 3, RSSI -67  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: R:26:42:F3:D5:A0:86, AD evt type 3, RSSI -73  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: R:0C:61:D1:B9:5D:9E, AD evt type 3, RSSI -87  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: R:20:C2:EE:59:85:5B, AD evt type 3, RSSI -66  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
[DEVICE]: R:25:3F:7A:EE:0F:55, AD evt type 3, RSSI -83  C:0 S:0 D:0 SR:0 E:0 Prim: LE 1M, Secn: No packets, Interval: 0x0000 (0 us), SID: 0xff
uart:~$ bt scan off
Scan successfully stopped
```

> 译注——扫描日志：DEVICE为设备，AD evt type为广播事件类型，RSSI为接收信号强度指示（Received Signal Strength Indicator）。C、S、D、SR、E分别标记可连接（Connectable）、可扫描（Scannable）、定向（Directed）、扫描响应（Scan Response）及扩展广播（Extended Advertising）；Prim／Secn为主／次物理层（Physical Layer，PHY），Interval为周期性广播间隔，SID为广播集标识（Advertising SID）。Bluetooth active scan enabled表示主动扫描已启用，Scan successfully stopped表示扫描已停止。地址、信号值和日志数量均为示例。

若结果过多，可以使用扫描过滤器（Scan Filter）缩小范围、寻找特定设备。原文列出按名称、RSSI、地址、周期性广播间隔四类过滤器，并写作 `bt scan-set-filter` 后接过滤类型；重复使用命令可增加多个过滤条件。

> 译注——拼写差异：正文中的 `bt scan-set-filter` 与下面示例不同；所读官方实现注册的是 `scan-filter-set`，即根提示符下使用 `bt scan-filter-set`。原文代码保留正确的示例拼写。

例如，只查找名称为 `test shell` 的设备：

```text
uart:~$ bt scan-filter-set name "test shell"
```

或者，查找很近的设备：

```text
uart:~$ bt scan-filter-set rssi -40
RSSI cutoff set at -40 dB
```

> 译注——信号阈值：原日志保留 `-40 dB`；RSSI此处表达接收功率水平，应按dBm理解。源码把低于−40的报告过滤掉，这不是精确距离测量，不能从阈值推出固定米数。

最后，删除全部过滤器：

```text
uart:~$ bt scan-filter-clear all
```

`bt scan on` 启动主动扫描（Active Scanning），扫描器会发送扫描请求包，向广播者索取更多信息。`bt scan passive` 启动被动扫描（Passive Scanning），不向广播者发出这种请求。

启用 [`CONFIG_BT_SCAN_EXT_FILTER_POLICY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCAN_EXT_FILTER_POLICY) 后，`bt scan --ext-filter-policy on` 以扩展扫描器过滤策略（Extended Scanner Filter Policy）启动扫描。控制器（Controller）此时还会上报目标地址为可解析私有地址（Resolvable Private Address，RPA）、但自身无法解析该目标地址的定向广播。其目标地址单独打印一行。这要求控制器支持扩展扫描器过滤策略，否则命令失败。

<a id="connecting-to-a-device"></a>

## 25.3\_连接设备（Connecting to a device）

连接前需知道设备地址及地址类型，将它们传给 `bt connect`。例如：

```text
uart:~$ bt connect R:52:84:F6:BD:CE:48
Connection pending
Connected: R:52:84:F6:BD:CE:48
Remote LMP version 5.3 (0x0c) subversion 0xffff manufacturer 0x05f1
LE Features: 0x000000000001412f
LE PHY updated: TX PHY LE 2M, RX PHY LE 2M
LE conn  param req: int (0x0018, 0x0028) lat 0 to 42
LE conn param updated: int 0x0028 lat 0 to 42
```

> 译注——地址和输出：`P:` 表示公共地址（Public Address），`R:` 表示随机地址（Random Address），示例把类型包含在地址字符串中。Connection pending为连接处理中，Connected为连接成功；随后输出远端链路管理协议（Link Manager Protocol，LMP）版本、LE特性、收发PHY及连接参数请求／更新。int、lat、to分别对应间隔、从机延迟和监督超时的原始参数值，不能把它们不加换算直接当成毫秒。

`bt connections` 列出当前活动连接，最大连接数由 [`CONFIG_BT_MAX_CONN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_CONN) 定义。使用 `bt disconnect <address: P:XX:XX:XX:XX:XX:XX or R:XX:XX:XX:XX:XX:XX>` 断开指定地址的连接。

**注意：**如果刚刚进行过扫描，可以直接执行不带地址的 `bt connect`，连接最后扫描到的设备。另一种方式是 `bt connect-name <name>`：自动启用名称过滤扫描，并连接第一个匹配项。

<a id="advertising"></a>

## 25.4\_广播（Advertising）

用 `bt advertise on` 开始广播。原文说明其默认参数使用可解析私有地址并携带设备名；若改用身份地址（Identity Address），执行 `bt advertise on identity`。用 `bt advertise off` 停止广播。

若要使用更高级的广播功能，先用 `bt adv-create` 创建广播者（Advertiser）。参数可在创建时传入，也可通过 `bt adv-param` 更新。随后用 `bt adv-start` 启动，用 `bt adv-stop` 停止。

自定义广播者可分别选择是否可连接、是否可扫描，因此有以下四种必选组合；创建或更新参数时都需要指定：

| 参数 | 是否可连接 | 是否可扫描 |
| --- | --- | --- |
| `conn-scan` | 是 | 是 |
| `conn-nscan` | 是 | 否 |
| `nconn-scan` | 否 | 是 |
| `nconn-nscan` | 否 | 否 |

创建并启动一个可连接、可扫描的广播者：

```text
uart:~$ bt adv-create conn-scan
Created adv id: 0, adv: 0x200022f0
uart:~$ bt adv-start
Advertiser[0] 0x200022f0 set started
```

该自定义广播者还没有广播设备名，需要添加。接着上例执行：

```text
uart:~$ bt adv-stop
Advertiser set stopped
uart:~$ bt adv-data dev-name
uart:~$ bt adv-start
Advertiser[0] 0x200022f0 set started
```

现在应能在广播数据中看到设备名。也可用 `name <custom name>` 替代 `dev-name`，设置自定义名称。`bt adv-data` 还允许手工设置原始广播数据；例如：

```text
uart:~$ bt adv-create conn-scan
Created adv id: 0, adv: 0x20002348
uart:~$ bt adv-data 1009426C7565746F6F74682D5368656C6C
uart:~$ bt adv-start
Advertiser[0] 0x20002348 set started
```

数据格式必须符合蓝牙核心规范（Bluetooth Core Specification）5.3版第3卷C部分第11节。此处第一个八位字节（Octet）表示后续长度，计入数据内容及1字节类型；第二字节 `0x09` 表示完整本地名称（Complete Local Name）；其余字节是名称的ASCII编码。另一台设备应看到名称 `Bluetooth-Shell`。

广播时，如果其他设备使用主动扫描，广播者可能收到扫描请求包。在广播者参数中加入 `scan-reports`，可以显示这些包。

<a id="directed-advertising"></a>

### 25.4.1\_定向广播（Directed Advertising）

若要重新连接已知设备，可以使用定向广播。下例中目标地址紧跟 `directed`；`low` 选择低占空比（Low Duty Cycle）模式。当远端启用了隐私功能，并支持解析定向广播中的目标地址时，需要使用 `dir-rpa`。

```text
uart:~$ bt adv-create conn-scan directed R:D7:54:03:CE:F3:B4 low dir-rpa
Created adv id: 0, adv: 0x20002348
```

此后启动该广播者，目标设备即可重新连接。

<a id="extended-advertising"></a>

### 25.4.2\_扩展广播（Extended Advertising）

使用 `ext-adv` 参数启用扩展广播：

```text
uart:~$ bt adv-create conn-nscan ext-adv
Created adv id: 0, adv: 0x200022f0
uart:~$ bt adv-start
Advertiser[0] 0x200022f0 set started
```

这会创建并启动一个可连接、不可扫描的扩展广播者。

<a id="encrypted-advertising-data"></a>

### 25.4.3\_加密广播数据（Encrypted Advertising Data）

Zephyr支持加密广播数据（Encrypted Advertising Data，EAD）。`bt encrypted-ad` 子命令用于管理指定广播者的数据。

加密前必须提供密钥材料：`bt encrypted-ad set-keys <session key> <init vector>` 设置16字节会话密钥（Session Key）和8字节初始化向量（Initialization Vector，IV）。

`bt encrypted-ad add-ad` 添加一个核心规范定义的广播数据结构；`bt encrypted-ad add-ead` 读取给定数据、加密后添加生成的加密广播数据结构。可以混合加密与未加密数据。添加完成后，用 `bt encrypted-ad commit-ad` 将修改应用到所选广播者，再按前文启动广播。`bt encrypted-ad clear-ad` 清空广播数据。

中心设备（Central）端先设置正确的密钥材料，然后执行 `bt encrypted-ad decrypt-scan on`，即可启用接收广播数据的解密。

**注意：**要在扫描报告中查看广播数据，需要启用 `bt scan-verbose-output`。

**注意：**可增大 [`CONFIG_BT_CTLR_ADV_DATA_LEN_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_DATA_LEN_MAX) 和 [`CONFIG_BT_CTLR_SCAN_DATA_LEN_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SCAN_DATA_LEN_MAX)，提高广播数据长度。

下面是原文的EAD示例，分别在外设（Peripheral）和中心设备端执行。

外设端：

```text
uart:~$ bt init
...
uart:~$ bt adv-create conn-nscan ext-adv
Created adv id: 0, adv: 0x81769a0
uart:~$ bt encrypted-ad set-keys 9ba22d3824efc70feb800c80294cba38 2e83f3d4d47695b6
session key set to:
00000000: 9b a2 2d 38 24 ef c7 0f  eb 80 0c 80 29 4c ba 38 |..-8$... ....)L.8|
initialisation vector set to:
00000000: 2e 83 f3 d4 d4 76 95 b6                          |.....v..         |
uart:~$ bt encrypted-ad add-ad 06097368656C6C
uart:~$ bt encrypted-ad add-ead 03ffdead03ffbeef
uart:~$ bt encrypted-ad commit-ad
Advertising data for Advertiser[0] 0x81769a0 updated.
uart:~$ bt adv-start
Advertiser[0] 0x81769a0 set started
```

中心设备端：

```text
uart:~$ bt init
...
uart:~$ bt scan-verbose-output on
uart:~$ bt encrypted-ad set-keys 9ba22d3824efc70feb800c80294cba38 2e83f3d4d47695b6
session key set to:
00000000: 9b a2 2d 38 24 ef c7 0f  eb 80 0c 80 29 4c ba 38 |..-8$... ....)L.8|
initialisation vector set to:
00000000: 2e 83 f3 d4 d4 76 95 b6                          |.....v..         |
uart:~$ bt encrypted-ad decrypt-scan on
Received encrypted advertising data will now be decrypted using provided key materials.
uart:~$ bt scan on
Bluetooth active scan enabled
[DEVICE]: R:68:49:30:68:49:30, AD evt type 5, RSSI -59   shell C:1 S:0 D:0 SR:0 E:1 Prim: LE 1M, Secn: LE 2M, Interval: 0x0000 (0 us), SID: 0x0
        [SCAN DATA START - EXT_ADV]
        Type 0x09:    shell
        Type 0x31: Encrypted Advertising Data: 0xe2, 0x17, 0xed, 0x04, 0xe7, 0x02, 0x1d, 0xc9, 0x40, 0x07, uart:~0x18, 0x90, 0x6c, 0x4b, 0xfe, 0x34, 0xad
        [START DECRYPTED DATA]
        Type 0xff: 0xde, 0xad
        Type 0xff: 0xbe, 0xef
        [END DECRYPTED DATA]
        [SCAN DATA END]
...
```

> 译注——EAD日志：session key set to及initialisation vector set to分别显示设置的密钥与IV；commit-ad后的updated表示广播数据已更新。接收日志中Type 0x09是名称，Type 0x31是EAD，START／END DECRYPTED DATA括起解密结果，两项Type 0xff为厂商专用数据。原日志中夹入的 `uart:~` 也按原样保留，不是要输入的参数。十六进制值来自公开示例，仅用于对照两端配置。

<a id="filter-accept-list"></a>

## 25.5\_过滤接受列表（Filter Accept List）

可以建立允许地址的列表，自动连接其中设备。例如：

```text
uart:~$ bt fal-add R:47:38:76:EA:29:36
uart:~$ bt fal-add R:66:C8:80:2A:05:73
uart:~$ bt fal-connect on
```

随后Shell连接第一个可用设备。原文说明，在该示例中，如果两个设备同时广播，会连接首先加入列表的地址。

> 译注——观察范围：这是原文给出的示例结果，不据此推导所有控制器和无线时序下都保证按列表插入顺序建立连接。

过滤接受列表（Filter Accept List，FAL）也能用于扫描或广播，参数为 `fal`。例如，仅扫描一组指定地址：

```text
uart:~$ bt fal-add R:65:4B:9E:83:AF:73
uart:~$ bt fal-add R:73:72:82:B4:8F:B9
uart:~$ bt fal-add R:5D:85:50:1C:72:64
uart:~$ bt scan on fal
```

此后应只看到这三个地址的扫描报告。

<a id="enabling-security"></a>

## 25.6\_启用安全（Enabling security）

连接设备后，可启用不同安全等级。原文对Bluetooth LE列出：

| 等级 | 原文含义 |
| --- | --- |
| 1 | 无加密（Encryption），无认证（Authentication）。 |
| 2 | 加密，但不认证。 |
| 3 | 加密并认证。 |
| 4 | Bluetooth LE安全连接（Secure Connection）。 |

> 译注——等级4的完整条件：[官方conn.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/conn.h)将 `BT_SECURITY_L4` 定义为经过认证的安全连接，并使用128位密钥；不能把原表简写理解为任何LE Secure Connections配对都已满足等级4。

用 `bt security <level>` 请求安全等级。等级3及以上要求认证，应先设置认证方法，例如执行 `bt auth all`。原文示例随后在两端要求确认口令（Passkey）；Shell端用 `bt auth-passkey-confirm` 确认。

<a id="pairing"></a>

## 25.7\_配对（Pairing）

原文写道，启用认证要求设备可绑定（Bondable）；Shell默认可绑定。可用 `bt bondable off` 关闭该状态，用 `bt bonds` 列出已配对设备。

> 译注——配对、认证和绑定：配对（Pairing）建立安全关系，绑定（Bonding）保留安全材料供后续使用，二者不能等同。[官方SMP实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/host/smp.c)分别设置认证与绑定标志，非绑定配对是否被拒绝还取决于 `CONFIG_BT_BONDING_REQUIRED` 等配置。因此上句不能推广成协议上“认证必然要求保存绑定”；`bt bonds` 管理的是已保存的绑定记录。

已配对设备数量上限由 [`CONFIG_BT_MAX_PAIRED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MAX_PAIRED) 设置。用 `bt clear <address: P:XX:XX:XX:XX:XX:XX or R:XX:XX:XX:XX:XX:XX>` 删除指定设备，或用 `bt clear all` 删除全部记录。


对应官方文档源码：[doc/services/connectivity/bluetooth/shell/host/gap.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/shell/host/gap.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/shell/host/gap.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<a id="tab-0-UGVyaXBoZXJhbA=="></a>
<a id="tab-0-Q2VudHJhbA=="></a>
<a id="panel-0-UGVyaXBoZXJhbA=="></a>
<a id="panel-0-Q2VudHJhbA=="></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：蓝牙Mesh接口](P024_蓝牙Mesh接口.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：GATT_Shell](P026_GATT_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P024_蓝牙Mesh接口.md) · [返回大纲](大纲.md) · [下一章](P026_GATT_Shell.md)

</details>

<!-- reading-navigation:end -->

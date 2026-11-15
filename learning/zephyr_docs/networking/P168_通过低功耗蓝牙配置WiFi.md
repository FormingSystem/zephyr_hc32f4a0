---
id: learning.zephyr-docs.networking.page-168
title: 通过低功耗蓝牙配置WiFi
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/wifi/ble_provisioning/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第168章\_通过低功耗蓝牙配置WiFi

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/wifi/ble_provisioning/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

设备首次启动时，广播一个自定义的通用属性配置文件（Generic Attribute Profile，GATT）服务，让低功耗蓝牙（Bluetooth Low Energy，BLE）中心设备（Central）写入 Wi-Fi 服务集标识符（Service Set Identifier，SSID）和预共享密钥（Pre-Shared Key，PSK）。收到控制命令后，设备通过[Wi-Fi 凭据库（Wi-Fi Credentials Library）](P164_WiFi凭据库.md#lib-wifi-credentials)保存凭据，再通过 `NET_REQUEST_WIFI_CONNECT_STORED` 加入网络。后续启动时使用已保存的凭据自动重连。

官方[示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/wifi/ble_provisioning)包含 GATT 服务、凭据处理及应用状态逻辑。

### 1.1 状态机（State Machine）

官方状态转换原图以纯文本表示，原样保留：

```text
IDLE --(SSID + PSK + CONNECT)--> CONNECTING --> CONNECTED
                                      \
                                       --> FAILED
```

`IDLE` 表示空闲，写入 SSID、PSK 并发送 `CONNECT` 后进入 `CONNECTING`（连接中），成功后为 `CONNECTED`（已连接），失败则为 `FAILED`。控制命令 `ERASE` 清除已保存凭据并返回 `IDLE`。

### 1.2 GATT 服务

所有特征（Characteristic）共用自定义 128 位基础 UUID `8b84xxxx-f6fa-4e33-9a0c-e14d9f35f201`，用下表中的短标识替换 `xxxx`：

| 特征（Char） | UUID 短标识 | 属性（Properties） | 载荷（Payload） |
| --- | --- | --- | --- |
| SSID | `0002` | 写（write） | UTF-8，最多 32 字节。 |
| Password（密码） | `0003` | 写（write） | UTF-8，最多 64 字节。 |
| Security（安全类型） | `0004` | 写（write） | 1 字节，可选，见下一表。 |
| Control（控制） | `0005` | 写（write） | 1 字节：`0x01` 为 CONNECT，`0x02` 为 ERASE。 |
| Status（状态） | `0006` | 读、通知（read, notify） | 1 字节枚举，见 `gatt_svc.h`。 |

原文称安全类型值与 [`wifi_security_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html#gadde31a04fa25ed805115c6b31854cd9c) 对应，列出以下映射：

| 字节值（Byte） | 原文含义（Meaning） |
| --- | --- |
| `0` | Open，开放网络，无密码。 |
| `1` | WPA2-PSK。 |
| `2` | WPA2-PSK-SHA256。 |
| `3` | WPA3-SAE。 |
| `6` | WPA-Auto-Personal，WPA2／WPA3 过渡模式。 |
| `0xFF` | 自动判断：PSK 为空则开放，否则 WPA2-PSK；默认值。 |

不写入 Security 特征时，设备回退到 `0xFF` 自动判断。

> 源码更正：原表的 `6` 与当前官方[枚举定义](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/wifi.h)不一致：`6` 是 `WIFI_SECURITY_TYPE_WAPI`，`10` 才是 `WIFI_SECURITY_TYPE_WPA_AUTO_PERSONAL`，其注释为 WPA／WPA2／WPA3 PSK。`3` 还对应 `WIFI_SECURITY_TYPE_SAE_HNP` 的别名，`4` 为 SAE-H2E，`5` 为 SAE-AUTO。当前[wifi_prov.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/src/wifi_prov.c)除 `0xFF` 外直接转换该字节为枚举，没有把 `6` 重映射成自动个人模式。使用该源码时，不要照原表把 `6` 当作 WPA2／WPA3 自动模式写入。

> 译注：这里“自动判断”只根据 PSK 是否为空选择开放网络或 WPA2-PSK，并不扫描和识别接入点支持的所有认证方式。长度限制按字节计算，不能按中文字符数理解。当前[gatt_svc.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/src/gatt_svc.c)拒绝非零写入偏移；示例配置提高了 ATT MTU，但中心设备仍需协商足够的 MTU，不能把长密码分成带偏移的多次写入来假定完成。

## 2. 要求（Requirements）

需要同时支持 Wi-Fi 和 Bluetooth LE 的开发板。

## 3. 构建与运行

在已配置 Zephyr 环境、具有目标开发板所需依赖的主机上，从读者自己的 Zephyr 源码根目录执行：

```sh
west build -b esp32c6_devkitc/esp32c6/hpcore samples/net/wifi/ble_provisioning
west flash
```

烧写后，设备以 `Zephyr Wi-Fi Provisioning` 名称开始广播，可通过 [`CONFIG_BT_DEVICE_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME) 修改名称。

### 3.1 使用 nRF Connect Mobile 测试

1. 在 Android 或 iOS 上安装 nRF Connect for Mobile。
2. 打开应用，点击 Scan（扫描），连接广播中的设备。
3. 展开自定义服务，基础 UUID 为 `8b840001-f6fa-4e33-9a0c-e14d9f35f201`。
4. 把 SSID 作为 UTF-8 字节写入 `0002` 特征。
5. 把密码写入 `0003` 特征。
6. 可选：把安全类型字节写入 `0004` 特征，数值应结合上面的源码更正核对。
7. 可选：启用 Status `0006` 特征的通知。
8. 向 Control `0005` 特征写入 `0x01`，请求 Wi-Fi 连接。
9. 观察串口控制台和 Status 通知，状态应经过 `CONNECTING (2)` 到达 `CONNECTED (3)`。
10. 要擦除已保存的凭据，向 Control 特征写入 `0x02`。

> 源码对照：当前[gatt_svc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/src/gatt_svc.h)定义完整状态为 `IDLE=0`、`PROVISIONED=1`、`CONNECTING=2`、`CONNECTED=3`、`FAILED=4`。值为 `1` 的枚举存在，不代表上述流程必然发送该状态。Wi-Fi 连接成功事件也不等于已经获得 IP 地址或能够访问互联网，仍需区分无线关联与后续网络配置。

## 4. 安全性（Security）

通过一个 Kconfig 选择项配置三种 BLE 安全模式：

| 模式 | 配置 | 原文行为 |
| --- | --- | --- |
| 无安全保护（None），默认 | [`CONFIG_WIFI_BLE_PROV_SECURITY_NONE`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/Kconfig) | 不配对，凭据明文传输，仅用于评估。 |
| 加密链路（Encrypted Link） | [`CONFIG_WIFI_BLE_PROV_SECURITY_ENCRYPT`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/Kconfig) | 写操作需要加密链路，无需用户交互即可配对；原文说明被动窃听者无法恢复凭据。 |
| 经过认证的配对（Authenticated Pairing） | [`CONFIG_WIFI_BLE_PROV_SECURITY_AUTH`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/Kconfig) | 写操作需要带加密和认证的 LE 安全连接（LE Secure Connections，LESC）配对。设备在控制台打印 6 位配对码（Passkey），中心设备必须输入它。 |

> 源码边界：当前[Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/Kconfig)将 ENCRYPT 标为无中间人攻击（Man-in-the-Middle，MITM）保护的加密模式；AUTH 才选择 `BT_SMP_SC_ONLY` 并要求认证。因此，不能把无需交互的加密配对理解为已经认证对端身份。原文对被动窃听的说明也不能扩展为抵抗所有配对攻击的保证。

原文指出，已保存的凭据仍以明文保存在非易失性存储（Non-Volatile Storage，NVS）中。要保护静态存储中的凭据（Credentials at Rest），可切换到 [`CONFIG_WIFI_CREDENTIALS_BACKEND_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS_BACKEND_PSA)，或采用厂商 NVS 加密。

> 译注：当前示例[prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/prj.conf)选择 Settings／NVS 后端。PSA 后端有平台及 TF-M 依赖，不能假定给任意 Wi-Fi 开发板添加一个配置项就能启用；应先核对[凭据库说明](P164_WiFi凭据库.md)。

> 原文提示：切换安全模式时会复用同一 NVS 分区。旧构建留下的 BLE 绑定（Bond）可能在启动时产生 `set-value failure` 警告，原文建议切换时使用 `west flash --erase` 擦除 Flash。该操作会清除持久化数据，应区分正常烧写与为清理旧绑定而进行的擦除；本次未执行。

> 源码对照：当前[应用逻辑](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/src/main.c)处理 ERASE 时还会清空待提交数据、删除 BLE 绑定，并在因配网成功停止广播后恢复广播；它没有同时调用 Wi-Fi 断开请求。凭据保存采用单槽配网语义：先删除全部旧条目再写入新条目，新保存失败并不自动恢复旧凭据。

## 5. 示例 Kconfig 选项

- [`CONFIG_BT_DEVICE_NAME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DEVICE_NAME)：广播设备名。
- [`CONFIG_WIFI_BLE_PROV_KEEP_BLE_AFTER_CONNECT`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/Kconfig)：Wi-Fi 连接后继续广播。
- [`CONFIG_WIFI_BLE_PROV_SECURITY_NONE`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/Kconfig)、[`CONFIG_WIFI_BLE_PROV_SECURITY_ENCRYPT`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/Kconfig)、[`CONFIG_WIFI_BLE_PROV_SECURITY_AUTH`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/ble_provisioning/Kconfig)：配网写操作所用的 BLE 安全模式。

## 6. 示例输出（Sample Output）

以下为官方原始日志，不是本次运行结果：

```console
*** Booting Zephyr OS build v4.4.0 ***
<inf> wifi_ble_prov: Wi-Fi BLE provisioning starting
<inf> wifi_ble_prov: security: none (plaintext)
<inf> gatt_svc: status -> 0
<inf> wifi_ble_prov: no stored credentials; waiting for provisioning over BLE
<inf> gatt_svc: advertising as 'Zephyr Wi-Fi Provisioning'
<inf> wifi_ble_prov: connected: R:4F:0D:14:E8:76:98
<inf> wifi_prov: connecting using stored credentials
<inf> gatt_svc: status -> 2
<inf> wifi_prov: Wi-Fi connected
<inf> gatt_svc: status -> 3
```

日志依次表明应用启动、当前安全模式为明文、暂无凭据而等待 BLE 配网、开始广播、中心设备连接、使用保存的凭据连接 Wi-Fi，以及状态由 `2` 变为 `3`。如果停在 `FAILED` 或未收到连接结果，应返回检查 SSID、口令、安全类型编号和设备 Wi-Fi 能力；不要只根据 BLE 写入成功判断 Wi-Fi 已连接。

## 7. 另见（See Also）

- [蓝牙 API（Bluetooth APIs）](https://docs.zephyrproject.org/latest/doxygen/html/group__bluetooth.html)。
- [Wi-Fi 管理（Wi-Fi Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html)。
- [Wi-Fi 凭据库 API（Wi-Fi Credentials Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__credentials.html)。

> 验证边界：本章已逐项核对 UUID、字段长度、原始命令与日志，并针对明确差异查阅官方源码；未构建、烧写、清除设备数据或实际进行 BLE／Wi-Fi 配网。


<a id="wifi-ble-provisioning"></a>
<a id="overview"></a>
<a id="state-machine"></a>
<a id="gatt-service"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="testing-with-nrf-connect-mobile"></a>
<a id="security"></a>
<a id="sample-kconfig-options"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P167_WiFi接入点与站点并行示例.md) · [返回大纲](大纲.md) · [下一章](P169_WiFi命令行示例.md)

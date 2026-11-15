---
id: learning.zephyr-docs.networking.page-163
title: WiFi管理接口
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/wifi.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第163章\_WiFi管理接口

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/wifi.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Wi-Fi 管理 API（Wi-Fi Management API）用于管理 Wi-Fi 网络，支持以下模式：

- IEEE 802.11 站点（Station，STA）。
- IEEE 802.11 接入点（Access Point，AP）。
- IEEE 802.11 点对点通信（Peer-to-Peer，P2P），即 Wi-Fi Direct。

原文概述称仅支持个人模式（Personal Mode）安全机制，并列出以下类型：开放网络（Open）、机会式无线加密（Opportunistic Wireless Encryption，OWE）、有线等效保密（Wired Equivalent Privacy，WEP）、WPA2-PSK、WPA2-PSK-256 和 WPA3-SAE。其中，WPA 是 Wi-Fi 保护访问（Wi-Fi Protected Access），PSK 是预共享密钥（Pre-Shared Key），SAE 是对等实体同时认证（Simultaneous Authentication of Equals）。

> 译注：这一“仅支持个人模式”的概述与同页后面的企业模式（Enterprise Mode）说明并不一致。当前官方[安全类型枚举](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/wifi.h)也包含多种 EAP 企业认证类型。这里保留原文范围声明，但不能用它否定后文企业认证功能；实际支持取决于所选驱动、网络管理实现和配置。

API 在网络二层（Layer 2，L2）协议栈的 `wifi_mgmt` 模块中实现。目前支持两类 Wi-Fi 驱动：网络或套接字卸载驱动（Networking or Socket Offloaded Drivers），以及原生 L2 以太网驱动（Native L2 Ethernet Drivers）。

### 1.1 编译功能（Compiled Features）

应用如果只需要 Wi-Fi 功能的某个子集，可以通过 [`CONFIG_WIFI_USAGE_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE) 向驱动提示需要编入哪些功能。可用提示包括：

| 配置 | 使用模式 |
| --- | --- |
| [`CONFIG_WIFI_USAGE_MODE_STA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_STA) | 连接到接入点。 |
| [`CONFIG_WIFI_USAGE_MODE_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_AP) | 作为接入点运行。 |
| [`CONFIG_WIFI_USAGE_MODE_STA_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_STA_AP) | 同时作为接入点并连接另一个接入点。 |
| [`CONFIG_WIFI_USAGE_MODE_SCAN_ONLY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_SCAN_ONLY) | 只扫描接入点的服务集标识符（Service Set Identifier，SSID）。 |

> 原文提示：请求的使用模式是否得到支持取决于硬件。配置提示并不会自动为缺少相应能力的设备增加支持。

### 1.2 Wi-Fi 命令行（Wi-Fi Shell）

Wi-Fi Shell 提供交互命令，用于测试和探索管理 API，无需专门编写应用。启用 [`CONFIG_NET_L2_WIFI_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_WIFI_SHELL) 即可加入 `wifi` 命令。

| 子命令（Subcommand） | 说明 |
| --- | --- |
| `scan` | 扫描 Wi-Fi 网络。 |
| `connect` | 连接 Wi-Fi 网络。 |
| `disconnect` | 断开 Wi-Fi 网络。 |
| `status` | 显示 Wi-Fi 接口状态。 |

使用 `wifi --help` 列出所有子命令，使用 `wifi <subcommand> --help` 查看具体命令的帮助。启用此功能的应用见[Wi-Fi 命令行示例（Wi-Fi Shell）](P169_WiFi命令行示例.md#wifi-shell)。

> 原文警告：扫描命令默认不限制结果数量。UART 命令行后端输出较慢，打印全部结果可能导致网络管理事件被丢弃。必要时调整 [`CONFIG_NET_MGMT_EVENT_QUEUE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_QUEUE_TIMEOUT) 或 [`CONFIG_NET_MGMT_EVENT_QUEUE_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT_QUEUE_SIZE)。

### 1.3 支持 PSA 密码 API 的构建

要在 Wi-Fi 构建中启用平台安全架构（Platform Security Architecture，PSA）密码 API，需设置 [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_ALT) 和 [`CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_NM_WPA_SUPPLICANT_CRYPTO_MBEDTLS_PSA)。

WPA3-SAE、设备配置协议（Device Provisioning Protocol，DPP）、SAE-PK、WPA2-PSK 和企业 EAP 等功能如何映射到大整数、椭圆曲线 Diffie–Hellman（Elliptic Curve Diffie–Hellman，ECDH）、TLS、散列和 AES，以及哪些路径采用传统密码 API（Legacy Crypto）或 PSA Crypto，见[Wi-Fi 功能与密码原语映射](P165_WiFi功能与密码原语映射.md)。

## 2. 企业模式测试：X.509 证书管理

Wi-Fi 企业安全认证需要 X.509 证书，支持构建时安装和运行时安装两种方式。下列主机命令按官方 Bash 风格保留；涉及 `samples/` 或 `scripts/` 的相对路径均从读者自己的 Zephyr 源码根目录解析。`<board>` 等尖括号内容是待替换参数，设备提示符后的 `wifi` 命令则在设备 Shell 中执行。

### 2.1 构建时证书（Compile Time Certificates）

PEM 格式测试证书位于官方仓库的[samples/net/wifi/test_certs](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/test_certs)。构建时将证书转换为供 Wi-Fi Shell 模块使用的 C 头文件。要使用自己的证书，可以在同一目录中替换现有文件：

```sh
$ export WIFI_TEST_CERTS_DIR=samples/net/wifi/test_certs/rsa3k
$ cp client.pem $WIFI_TEST_CERTS_DIR
$ cp client-key.pem $WIFI_TEST_CERTS_DIR
$ cp ca.pem $WIFI_TEST_CERTS_DIR
$ cp client2.pem $WIFI_TEST_CERTS_DIR
$ cp client-key2.pem $WIFI_TEST_CERTS_DIR
$ cp ca2.pem $WIFI_TEST_CERTS_DIR
$ west build -p -b <board> samples/net/wifi -S wifi-enterprise
```

使用 RSA 2048 位证书时，选择 `rsa2k_no_des`：

```sh
$ export WIFI_TEST_CERTS_DIR=samples/net/wifi/test_certs/rsa2k_no_des
```

也可以设置 `WIFI_TEST_CERTS_DIR`，使其指向保存证书的目录。原文紧接着给出的命令通过 CMake `-D` 参数传值：

```sh
$ west build -p -b <board> samples/net/wifi -S wifi-enterprise -- -DWIFI_TEST_CERTS_DIR=<path_to_your_certificates>
```

> 译注：上述前两条构建示例仍以 `samples/net/wifi` 为应用路径；当前该位置是示例目录入口，Wi-Fi Shell 应用在 `samples/net/wifi/shell`。当前[企业模式配置片段](https://github.com/zephyrproject-rtos/zephyr/blob/main/snippets/wifi/wifi-enterprise/snippet.yml)仍名为 `wifi-enterprise`。使用当前源码时，应把构建命令的应用路径改为 `samples/net/wifi/shell`，保留所需的 `-S wifi-enterprise` 和证书目录参数；不要把目录索引当作可构建应用。

> 源码对照：当前[证书生成逻辑](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/CMakeLists.txt)通过 `zephyr_get(WIFI_TEST_CERTS_DIR SYSBUILD GLOBAL)` 读取目录，未指定时使用源码中的 `samples/net/wifi/test_certs/rsa3k`。它逐项处理 8 个证书／密钥文件，文件不存在时会生成带说明的空 `.inc` 文件。因此，生成文件存在不能证明证书内容有效，仍需核对所选 EAP 方法实际需要的材料。

### 2.2 运行时证书（Run Time Certificates）

Wi-Fi Shell 使用 TLS 凭据子系统（TLS Credentials Subsystem）存储和管理证书。证书可以通过 Shell 在运行时添加，详见[TLS 凭据命令行](P042_TLS凭据Shell.md#tls-credentials-shell)。示例或应用需启用 [`CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_SHELL_RUNTIME_CERTIFICATES)。

官方提供安装辅助脚本，原文用法如下：

```sh
$ ./scripts/utils/wifi_ent_cert_installer.py -p samples/net/wifi/test_certs/rsa2k_no_des
```

该脚本通过 UART 发送 TLS 凭据命令，把证书安装到设备的凭据存储中。

> 源码对照：当前[安装脚本](https://github.com/zephyrproject-rtos/zephyr/blob/main/scripts/utils/wifi_ent_cert_installer.py)要求 `--path`，并设置 `allow_abbrev=False`，没有 `-p` 别名，因此原文短参数与当前脚本不匹配。当前调用应使用 `--path samples/net/wifi/test_certs/rsa2k_no_des`；串口由 `--serial-device` 指定。脚本默认串口 `/dev/ttyACM1` 是 Linux 设备节点示例，不是仓库位置，也不适用于所有主机。脚本还从当前目录调用 `./scripts/utils/tls_creds_installer.py`，因此需在 Zephyr 源码根目录执行。默认 STA 模式处理两组客户端材料，`--operation-mode AP` 处理接入点材料；缺少文件会跳过，单个子进程安装失败也会继续，最后的“安装过程完成”日志不代表所有证书均已安装。

按可扩展认证协议（Extensible Authentication Protocol，EAP）方法选择连接命令：

- EAP-TLS：

```console
uart:~$ wifi connect -s <SSID> -c <channel> -k 7 -w 2 -a <Anonymous identity> --key1-pwd <Password EAP phase1> --key2-pwd <Password EAP phase2>
```

- EAP-TTLS-MSCHAPV2：

```console
uart:~$ wifi connect -s <SSID> -c <channel> -k 14 -K <Private key Password> --eap-id1 <Client Identity> --eap-pwd1 <Client Password> -a <Anonymous identity>
```

- EAP-PEAP-MSCHAPV2：

```console
uart:~$ wifi connect -s <SSID> -c <channel> -k 12 -K <Private key Password> --eap-id1 <Client Identity> --eap-pwd1 <Client Password> -a <Anonymous identity>
```

同一目录还提供用于测试的服务器证书。可使用任意认证、授权和计费（Authentication, Authorization and Accounting，AAA）服务器，例如 `FreeRADIUS` 或 `hostapd`。

### 2.3 服务器证书域名验证

原文说明：通过服务器提供的 X.509 证书中的通用名称（Common Name，CN）字段验证认证服务器身份。精确域名匹配（Exact Domain Match）要求 CN 与指定域名完全相同；域名后缀匹配（Domain Suffix Match）允许 CN 以指定域名后缀结尾。

采用精确匹配的原文命令：

```console
wifi connect -s <SSID> -c <channel> -k 12 -K <Private key Password> -e <Domain match>
```

采用后缀匹配的原文命令：

```console
wifi connect -s <SSID> -c <channel> -k 12 -K <Private key Password> -x <Domain suffix name>
```

> 源码对照：上述 CN 描述有所简化。当前清单固定的 hostap [tls_mbedtls_alt.c](https://github.com/zephyrproject-rtos/hostap/blob/33921a8a77c56bddfe196a11935009cededc3bb3/src/crypto/tls_mbedtls_alt.c)中，`tls_mbedtls_match_suffixes()` 先检查主题备用名称（Subject Alternative Name，SAN）中的 DNS 名称，再检查 CN。后缀比较不区分大小写，允许完整相等，或在域名点分隔边界匹配子域；并非任意字符串尾部相同就可通过。域名匹配也不能代替证书链验证。示例中的身份、口令和域名仍需按所选 EAP 方法补全。

### 2.4 不同 EAP 方法需要哪些证书

- EAP-TLS：客户端同时需要客户端证书及其私钥、证书颁发机构（Certificate Authority，CA）证书。客户端使用自己的证书向服务器证明身份。
- EAP-TTLS-MSCHAPV2：客户端只需 CA 证书，通过 TLS 隧道中的用户名和密码执行 MSCHAPV2 认证，无需客户端证书。
- EAP-PEAP-MSCHAPV2：与 TTLS 类似，通过 TLS 隧道中的用户名和密码执行 MSCHAPV2，无需客户端证书。

> 原文提示：仓库中的证书仅供测试，不能用于生产。它们由[FreeRADIUS raddb 脚本](https://github.com/FreeRADIUS/freeradius-server/tree/master/raddb/certs)生成。

> 原文提示：TLS 凭据子系统默认选择易失性后端 [`CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS_BACKEND_VOLATILE)，证书保存在 RAM 中，重启后丢失，需重新安装。可改用受保护存储（Protected Storage，PS）后端 [`CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS_BACKEND_PROTECTED_STORAGE)，把证书存入非易失性存储。

### 2.5 使用 FreeRADIUS 生成测试证书

`samples/net/wifi/test_certs/rsa2k_no_des` 中的测试证书由[FreeRADIUS raddb/certs 脚本](https://github.com/FreeRADIUS/freeradius-server/tree/master/raddb/certs)生成。自行生成时按原文执行以下步骤：

1. 安装 OpenSSL 和 GNU Make，下载[raddb/certs 目录](https://github.com/FreeRADIUS/freeradius-server/tree/master/raddb/certs)。
2. 在该目录编辑 `Makefile`，为服务器和客户端私钥的 OpenSSL 命令添加 `-nodes`。原文称这是为了生成不受密码保护的私钥，因为“Zephyr Wi-Fi Shell 不支持私钥密码”：

```makefile
$(OPENSSL) req -new -out server.csr -keyout server.key -nodes -config ./server.cnf
$(OPENSSL) req -new -out client.csr -keyout client.key -nodes -config ./client.cnf
```

3. 可选：按环境需要修改 `server.cnf` 和 `client.cnf`。
4. 在 `raddb/certs` 目录生成证书：

```sh
make destroycerts
make server
make client
```

5. 按下表重命名，匹配 Zephyr 示例的文件名。原表以两列多行呈现，此处逐文件列出相同对应关系：

| FreeRADIUS 输出 | Zephyr 示例名称 |
| --- | --- |
| `ca.pem` | `ca.pem` |
| `server.key` | `server-key.pem` |
| `server.pem` | `server.pem` |
| `client.key` | `client-key.pem` |
| `client.pem` | `client.pem` |

6. 将重命名后的文件复制到自己的 Zephyr 工程证书目录，例如 `samples/net/wifi/test_certs/rsa2k_no_des`。原文要求使用 AES（PBES2）加密私钥，不使用 DES，并以现有 `rsa2k_no_des` 密钥为参考。

> 译注：原文第 2 步“不使用私钥密码”与第 6 步“加密私钥”存在矛盾。当前[Wi-Fi Shell 实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/wifi/wifi_shell.c)已解析 `--key1-pwd`、`--key2-pwd` 并填入私钥密码字段，与本章前面的连接示例一致。因此不能把“不支持私钥密码”当作当前所有配置的结论；应使实际密钥格式、密码和所选密码后端相匹配。`make destroycerts` 会清理当前证书工作目录内的生成材料，应只在用于生成测试材料的目录运行。本次仅翻译和源码核对，没有运行这些生成／清理命令。

> 原文再次强调：这些证书仅供测试，不能用于生产。

## 3. Wi-Fi P2P（Wi-Fi Direct）

Wi-Fi P2P 允许设备直接互相通信，无需传统接入点，适合设备间通信场景。启用并构建 P2P 支持：

```sh
$ west build -p -b <board> samples/net/wifi/shell -- -DCONFIG_WIFI_NM_WPA_SUPPLICANT_P2P=y
```

## 4. 邻近感知网络（Neighbor Awareness Networking，NAN）

Wi-Fi NAN 又称 Wi-Fi Aware，允许设备在没有传统接入点或互联网连接的情况下发现服务并与附近设备通信。它采用发布—订阅（Publish–Subscribe）模型：设备可以发布服务，也可以通过订阅发现邻近设备的服务。启用并构建 NAN 支持：

```sh
$ west build -p -b <board> samples/net/wifi/shell -- -DCONFIG_WIFI_NM_WPA_SUPPLICANT_NAN=y
```

## 5. API 参考与相关示例

完整接口入口为[Wi-Fi 管理 API 参考（Wi-Fi Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html)，其自动生成子页单独跟踪翻译状态。本章的命令、证书和 Shell 介绍不代替完整 API 定义。

- [Wi-Fi AP-STA 模式示例](P167_WiFi接入点与站点并行示例.md#wifi-ap-sta-mode)：把支持的开发板配置为同时运行接入点与站点。
- [通过低功耗蓝牙配置 Wi-Fi](P168_通过低功耗蓝牙配置WiFi.md#wifi-ble-provisioning)：通过 BLE GATT 服务接收凭据并连接接入点。

> 验证边界：本章已核对官方页面及明确列出的源码，没有构建或烧写任何开发板，没有安装证书、连接网络或进行实板认证测试。网页 latest 与当前 main 可能处于不同修订，差异按译注明示。


<a id="wi-fi-management"></a>
<a id="wifi-mgmt"></a>
<a id="overview"></a>
<a id="compiled-features"></a>
<a id="wi-fi-shell"></a>
<a id="id1"></a>
<a id="wi-fi-psa-crypto-supported-build"></a>
<a id="wi-fi-feature-to-crypto-mapping"></a>
<a id="wi-fi-enterprise-test-x-509-certificate-management"></a>
<a id="compile-time-certificates"></a>
<a id="index-0"></a>
<a id="run-time-certificates"></a>
<a id="server-certificate-domain-name-verification"></a>
<a id="certificate-requirements-for-eap-methods"></a>
<a id="how-to-generate-test-certificates-using-freeradius"></a>
<a id="wi-fi-p2p-wi-fi-direct"></a>
<a id="wifi-mgmt-p2p"></a>
<a id="wi-fi-nan-neighbor-awareness-networking"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：网络系统管理目录](P162_网络系统管理目录.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：WiFi凭据库](P164_WiFi凭据库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P162_网络系统管理目录.md) · [返回大纲](大纲.md) · [下一章](P164_WiFi凭据库.md)

</details>

<!-- reading-navigation:end -->

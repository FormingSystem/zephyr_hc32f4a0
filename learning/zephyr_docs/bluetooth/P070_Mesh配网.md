---
id: learning.zephyr-docs.bluetooth.page-70
title: Mesh配网
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/provisioning.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="provisioning"></a>

<a id="bluetooth-mesh-provisioning"></a>

# 第70章\_配网（Provisioning）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/provisioning.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：配网器（provisioner）负责把设备加入网络，待配网设备（provisionee）是被加入的一方；带外（OOB）表示通过配网链路之外的途径交换信息。配网完成不等于模型已绑定应用密钥或配置好发布与订阅，后续配置见[配置数据库](P074_Mesh配置数据库.md)。

配网是把设备加入 Mesh 网络的过程，需要两台设备分别承担以下角色：

- 配网器（provisioner）代表网络所有者，负责把新节点加入 Mesh 网络。

- 待配网设备（provisionee）是通过配网过程加入网络的设备。在过程开始前，它是未配网设备（unprovisioned device）。

Zephyr Bluetooth Mesh 协议栈的配网模块为待配网设备角色同时支持广播配网承载（Advertising Provisioning bearer）与 GATT 配网承载（GATT Provisioning bearer），并为配网器角色支持广播配网承载。

<a id="the-provisioning-process"></a>

## 70.1 配网过程（The Provisioning process）

所有 Bluetooth Mesh 节点都必须先完成配网才能参与网络。配网 API 提供设备成为已配网 Mesh 节点所需的全部功能。配网分为以下五步：

- 信标广播（Beaconing）

- 邀请（Invitation）

- 公钥交换（Public key exchange）

- 身份认证（Authentication）

- 配网数据传输（Provisioning data transfer）

<a id="beaconing"></a>

### 70.1.1 信标广播（Beaconing）

要开始配网，未配网设备首先广播未配网信标（Unprovisioned Beacon），让附近的配网器发现它并发起配网。调用 [`bt_mesh_prov_enable()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga6c8dc1b09d4cde8738be83c992b860a9) 表示设备需要配网；设备会广播包含设备 UUID 和 `OOB information` 字段的信标，这些内容由传给 [`bt_mesh_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga521def6f74467a9bd3f2757c6aabd405) 的 `prov` 参数指定。此外，还可指定统一资源标识符（Uniform Resource Identifier，URI），指向带外信息的位置，例如设备公钥或认证值数据库。URI 在独立信标中广播，未配网信标则包含 URI 哈希，将两者关联起来。

<a id="uniform-resource-identifier"></a>

#### 70.1.1.1 统一资源标识符（Uniform Resource Identifier）

URI 应遵循《Bluetooth Core Specification Supplement》规定的格式，以编码为单个 UTF-8 数据点的 URI 方案开头；也可使用编码为 `0x01` 的特殊 `none` 方案。可用方案列在[蓝牙网站（Bluetooth website）](https://www.bluetooth.com/specifications/assigned-numbers/)上。

> 译注——外链状态：原文的 URI 方案映射旧链接本次直接请求返回 403，网页读取也未成功。可从[Bluetooth SIG 分配编号入口](https://www.bluetooth.com/specifications/assigned-numbers/)继续查找；该入口目前链接的[URI 方案与格式页](https://www.bluetooth.com/specifications/uri-schemes-and-formats/)不是这里单字节方案编码表的逐项替代。下表保留本次 Zephyr 原文给出的编码示例。

编码后的 URI 示例：

<a id="id1"></a>

**URI 编码示例（URI encoding examples）**

| URI | 编码结果（Encoded） |
| --- | --- |
| `http://example.com` | `\x16//example.com` |
| `https://www.zephyrproject.org/` | `\x17//www.zephyrproject.org/` |
| `just a string` | `\x01just a string` |

<a id="provisioning-invitation"></a>

### 70.1.2 配网邀请（Provisioning invitation）

配网器通过发送配网邀请发起过程。若待配网设备支持健康服务端的[关注状态（Attention state）](P079_Mesh健康服务端.md#bluetooth-mesh-models-health-srv-attention)，邀请会使它通过该状态提示用户注意此设备。

未配网设备自动回应邀请，报告自己的能力列表，包括支持的带外认证方式和算法。

<a id="public-key-exchange"></a>

### 70.1.3 公钥交换（Public key exchange）

配网开始前，配网器与未配网设备通过带内（in-band）或带外（Out Of Band，OOB）方式交换公钥。

带内公钥交换属于配网过程的一部分，未配网设备和配网器始终支持。

如果应用希望支持 OOB 公钥交换，必须向 Mesh 协议栈提供公钥与私钥；未配网设备会在能力信息中表明这一点。配网器通过可用的带外机制取得公钥，例如设备广播包含公钥的数据包，或把公钥编码在设备包装上的二维码中。即使未配网设备已指定带外公钥，配网器无法通过 OOB 取得它时，仍可选择带内交换；此时协议栈会为每次配网生成新的密钥对。

要让未配网设备支持 OOB 公钥，必须启用 [`CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_PROV_OOB_PUBLIC_KEY)。应用必须在配网开始前初始化 [`bt_mesh_prov.public_key_be`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html#a1261ba69e785f005d5834ac49da00778) 和 [`bt_mesh_prov.private_key_be`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html#a1ab714e9be35242e02099884c3af45f5) 指针，提供公私钥；密钥字节必须采用大端序（big-endian）。

配网器端调用 [`bt_mesh_prov_remote_pub_key_set()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gae33b5b6e9650b49d46494b4a81b18674)，提交通过 OOB 获得的设备公钥。

<a id="authentication"></a>

### 70.1.4 身份认证（Authentication）

初始交换后，配网器选择带外（OOB）认证方式，使用户能够确认连接的确实是目标设备，而非恶意第三方。

配网 API 为待配网设备支持以下认证方式：

- 静态 OOB（Static OOB）：生产时为设备分配认证值，配网器通过应用特定方式查询该值。原文指出，使用 BTM_ECDH_P256_HMAC_SHA256_AES_CCM 算法安全配网时，静态 OOB 值应包含超过 128 位的熵，以提供足够的抗攻击能力。

- 输入 OOB（Input OOB）：用户输入认证值，可用输入动作见 [`bt_mesh_input_action_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaf71f3dbdef6b8c085e9a4f068e1f60c5)。

- 输出 OOB（Output OOB）：向用户显示认证值，可用输出动作见 [`bt_mesh_output_action_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga5512b81ef7eeb45b0a12ef62234c8795)。

应用必须在 [`bt_mesh_prov`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html) 中为支持的认证方式提供回调，并在 [`bt_mesh_prov.output_actions`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html#a8b88959c5eef7f47591468e9c9768b7c) 和 [`bt_mesh_prov.input_actions`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html#af928a9419f684bcbda0563dda2c34d76) 中启用相应动作。

选择输出 OOB 动作时，应在输出回调被调用后向用户呈现认证值，并保持到 [`bt_mesh_prov.input_complete`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html#a2717ddf38465b95452724078f780f9e5) 或 [`bt_mesh_prov.complete`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html#ad55abc2b1632455bb23fbd8b03df85ea) 回调触发为止。动作是 `blink`、`beep` 或 `vibrate` 时，应间隔至少三秒重复该序列。

选择输入 OOB 动作时，应用收到 [`bt_mesh_prov.input`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html#a31eff9c903ac721bbca7ab586dda9e80) 回调后应提示用户，并通过 [`bt_mesh_input_string()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga2592abf429b40ef9242bce26f5bd085e) 或 [`bt_mesh_input_numeric()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gabc9d68157928c2b343eddd08ef314d27) 把用户响应交回配网 API。60 秒内未记录到用户响应时，配网过程终止。

若待配网设备要强制要求 OOB 认证，必须使用 BT_MESH_ECDH_P256_HMAC_SHA256_AES_CCM 算法。

> 译注——名称对照：本页上方静态 OOB 段落写作 `BTM_ECDH_P256_HMAC_SHA256_AES_CCM`，此处写作 `BT_MESH_ECDH_P256_HMAC_SHA256_AES_CCM`。配置时应以[官方 Mesh Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/Kconfig)中的选项为准，不应按前一处拼写创建新配置。

<a id="data-transfer"></a>

### 70.1.5 数据传输（Data transfer）

设备身份认证成功后，配网器传输以下配网数据：

- 单播地址（Unicast address）

- 网络密钥（network key）

- IV 索引（IV index）

- 网络标志（Network flags）

  - 密钥刷新（Key refresh）

  - IV 更新（IV update）

此外，还会为节点生成设备密钥（device key）。所有这些数据由协议栈保存，随后调用配网完成回调 [`bt_mesh_prov.complete`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html#ad55abc2b1632455bb23fbd8b03df85ea)。

<a id="provisioning-security"></a>

## 70.2 配网安全（Provisioning security）

配网过程是否安全，取决于公钥交换机制与认证方式的选择。

2021 年 5 月 24 日，ANSSI [披露](https://kb.cert.org/vuls/id/799380)了一组 Bluetooth Mesh 配网协议漏洞：闪烁、振动、按压、旋转及输入／输出数字 OOB 方式提供的熵较低，可被用于冒充和中间人（MITM）攻击。由于 AuthValue 可被实时暴力破解，Bluetooth SIG 在《Bluetooth Mesh Profile Specification v1.0.1》的[勘误 16350](https://www.bluetooth.org/docman/handlers/DownloadDoc.ashx?doc_id=516072) 中把这些 OOB 方式重新归为不安全。为确保安全配网，应用应使用静态 OOB 值和带外公钥传输。

<a id="api-reference"></a>

## 70.3 API 参考（API reference）

[配网（Provisioning）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/provisioning.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/provisioning.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/provisioning.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh消息](P069_Mesh消息.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh代理](P071_Mesh代理.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P069_Mesh消息.md) · [返回大纲](大纲.md) · [下一章](P071_Mesh代理.md)

</details>

<!-- reading-navigation:end -->

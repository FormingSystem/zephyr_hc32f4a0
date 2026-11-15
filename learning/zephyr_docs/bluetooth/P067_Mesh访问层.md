---
id: learning.zephyr-docs.bluetooth.page-67
title: Mesh访问层
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/access.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="access-layer"></a>

<a id="bluetooth-mesh-access"></a>

# 第67章\_访问层（Access layer）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/access.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：元素（element）有单播地址，模型（model）定义行为；模型的订阅（subscription）决定接收哪些组／虚拟地址的消息，发布（publication）则决定主动发送的目的地址和参数。下述组成数据是节点声明，不是运行时自动探测硬件的结果。

访问层是应用访问 Bluetooth Mesh 网络的接口，提供把节点行为划分为元素（element）和模型（model）的机制；这些元素和模型由应用实现。

<a id="mesh-models"></a>

## 67.1 Mesh 模型（Mesh models）

Mesh 节点的功能由模型表示。一个模型实现节点支持的一种行为，例如灯、传感器或恒温器。模型按元素分组，每个元素有自己的单播地址（unicast address），每种类型的模型最多包含一个。通常，一个元素表示节点行为的一个方面。例如，一个包含传感器、两盏灯和一个电源插座的节点，可把功能分配给四个元素，每个元素实例化实现其中一种行为所需的全部模型。

节点的元素与模型结构在节点组成数据（Composition Data）中描述，初始化时传给 [`bt_mesh_init()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh.html#ga521def6f74467a9bd3f2757c6aabd405)。Bluetooth SIG 定义了一组基础模型，见 Mesh 模型，以及[《Bluetooth Mesh Model Specification》](https://www.bluetooth.com/specifications/mesh-specifications/)中用于实现常见行为的一组模型。所有未经 Bluetooth SIG 定义的模型都是厂商模型（vendor model），必须关联公司标识（Company ID）。 相关链接：[Mesh 模型（Mesh models）](P068_Mesh模型.md#bluetooth-mesh-models)。

Mesh 模型有多个参数，可通过协议栈初始化或[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)配置：

<a id="opcode-list"></a>

### 67.1.1 操作码列表（Opcode list）

操作码列表包含模型能接收的所有消息操作码，以及最小可接受载荷长度和处理回调。模型支持的操作码数量不限，但同一元素内每个操作码只能出现在一个模型中。

完整操作码列表必须通过组成数据中的模型结构传入，运行时不可更改。列表以特殊条目 [`BT_MESH_MODEL_OP_END`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf2c164506c601214c85d451747176827) 结束；除空列表外，都必须有此条目。空列表应使用 [`BT_MESH_MODEL_NO_OPS`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gae6d55e0a27bb7c448affd312a2e11656)，而不是定义普通操作码列表。

<a id="appkey-list"></a>

### 67.1.2 应用密钥列表（AppKey list）

AppKey 列表包含模型接收消息时可使用的全部应用密钥（application key）。只有使用列表内应用密钥加密的消息才会交给该模型。

每个模型可持有的应用密钥数量上限由 [`CONFIG_BT_MESH_MODEL_KEY_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_MODEL_KEY_COUNT) 配置。AppKey 列表的内容由配置服务端管理。 相关链接：[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

<a id="subscription-list"></a>

### 67.1.3 订阅列表（Subscription list）

在所用应用密钥位于 AppKey 列表中的前提下，模型处理发往其所属元素单播地址的全部消息；也处理发往其订阅列表中任意组地址（group address）或虚拟地址（virtual address）的数据包。这样，一个节点可用一条消息寻址网络中的多个节点。

每个模型的订阅列表可容纳的地址数量上限由 [`CONFIG_BT_MESH_MODEL_GROUP_COUNT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_MODEL_GROUP_COUNT) 配置，列表内容由配置服务端管理。 相关链接：[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

<a id="model-publication"></a>

### 67.1.4 模型发布（Model publication）

模型可以用两种方式发送消息：

- 在 [`bt_mesh_msg_ctx`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__msg__ctx.html) 中指定一组消息参数，然后调用 [`bt_mesh_model_send()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga7cac052ef76f4b37a95343329b078e77)。

- 设置 [`bt_mesh_model_pub`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__pub.html) 结构，然后调用 [`bt_mesh_model_publish()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga06644f8a5fa43351328d3f3403dbad03)。

通过 [`bt_mesh_model_publish()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga06644f8a5fa43351328d3f3403dbad03) 发布消息时，模型使用配置服务端设置的发布参数。对于未经请求而主动发送的模型消息，推荐使用这种方式，因为消息参数的选择责任交给了网络管理员；管理员通常比单个节点更了解整个 Mesh 网络。 相关链接：[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

为支持带发布参数的发布，模型必须分配发布用的数据包缓冲区，并通过 [`bt_mesh_model_pub.msg`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__pub.html#a5f5639c01d3704ec3d527c418d35f827) 传入。配置服务端也可为该消息设置周期发布。为支持周期发布，模型必须提供 [`bt_mesh_model_pub.update`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__pub.html#a0354344e08e633dc4d6c0b4e7b169080) 回调；它在消息发布前调用，使模型可按当前状态更新载荷。 相关链接：[`bt_mesh_model_pub.update`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__pub.html#a0354344e08e633dc4d6c0b4e7b169080)。

将 [`bt_mesh_model_pub.retr_update`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__pub.html#a16c13e46c012ab836acd02b8fe5f05e3) 设为 1，可使每次重传都触发 [`bt_mesh_model_pub.update`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__pub.html#a0354344e08e633dc4d6c0b4e7b169080) 回调。例如，使用 Delay 参数的模型可在每次重传时调整它。[`bt_mesh_model_pub_is_retransmission()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga1b961d45f8b7c231c698ca229115e434) 用于区分首次发布和重传；[`BT_MESH_PUB_MSG_TOTAL`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga230538bb39ac3d6c8c0327d1fad77e69) 与 [`BT_MESH_PUB_MSG_NUM`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga115ee29aba3c3e985aa11d6692ca0d83) 宏分别返回一个发布间隔内的总传输次数和重传序号。

<a id="extended-models"></a>

### 67.1.5 扩展模型（Extended models）

Bluetooth Mesh 规范允许模型彼此扩展。模型扩展另一模型时，会继承其功能；因此可复用已有功能，把简单模型组合成复杂模型，避免定义新的操作码。模型可扩展来自任意元素的任意数量模型。同一元素内发生扩展时，两模型共享订阅列表：协议栈把两个列表合并为一个，合并后的总订阅容量为原容量之和。模型还可扩展已扩展其他模型的模型，形成扩展树（extension tree）；树覆盖的每个元素各有一个共享订阅列表。

模型扩展在初始化期间调用 [`bt_mesh_model_extend()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf6356f715c8968151b8d539f2dd1880c) 完成。一个模型只能被另一个模型扩展一次，且不能形成循环。节点状态绑定及模型之间的其他关系仍须由模型实现自行定义。

模型扩展会给访问层数据包处理增加一定开销，必须显式启用 [`CONFIG_BT_MESH_MODEL_EXTENSIONS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_MODEL_EXTENSIONS) 才会生效。

<a id="model-data-storage"></a>

### 67.1.6 模型数据存储（Model data storage）

Mesh 模型可能有与实例关联且需要持久化的数据。访问层 API 利用内部模型实例编码机制提供存储支持。调用 [`bt_mesh_model_data_store()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gadff0895c5c34928d778fa615512b3d85) 可为每个实例保存一条用户定义数据。要在下次设备重启时读回，模型必须提供 [`bt_mesh_model_cb.settings_set`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__cb.html#a21fc24829c6933a035b0f0be1a1f58e5) 回调；持久化存储中发现模型专用数据时，该回调会被调用。模型可调用传入的 `read_cb` 读取数据，详情见[设置模块（Settings）](../storage/P005_设置子系统.md#settings-api)文档。

模型数据频繁变化时，每次变化都保存会增加 Flash 磨损。模型可调用 [`bt_mesh_model_data_store_schedule()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga762896dd2e806b5be061b220d53ce4db) 延后写入；协议栈按 [`CONFIG_BT_MESH_STORE_TIMEOUT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_STORE_TIMEOUT) 定义的延迟安排工作项。执行时，协议栈为每个提出存储请求的模型调用 [`bt_mesh_model_cb.pending_store`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__cb.html#ae28f875dffc7f5f2ce99abe590369f43) 回调；模型随后可调用 [`bt_mesh_model_data_store()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gadff0895c5c34928d778fa615512b3d85) 保存数据。

启用 [`CONFIG_BT_MESH_SETTINGS_WORKQ`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_SETTINGS_WORKQ) 后，[`bt_mesh_model_cb.pending_store`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__cb.html#ae28f875dffc7f5f2ce99abe590369f43) 回调从专用线程执行，允许协议栈在存储模型数据时处理其他收发消息。需保存大量数据时，建议启用此选项并使用 [`bt_mesh_model_data_store_schedule()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga762896dd2e806b5be061b220d53ce4db)。

<a id="composition-data"></a>

### 67.1.7 组成数据（Composition Data）

组成数据提供 Mesh 设备的信息，包括设备上的元素、支持的模型和其他功能。数据划分为不同页面，每页包含特定的设备功能信息。用户可通过配置服务端模型获取这些信息；若设备支持，也可通过[大型组成数据服务端（Large Composition Data Server）](P081_Mesh大型组成数据服务端.md#bluetooth-mesh-lcd-srv)模型获取。 相关链接：[配置服务端（Configuration Server）](P077_Mesh配置服务端.md#bluetooth-mesh-models-cfg-srv)。

<a id="composition-data-page-0"></a>

#### 67.1.7.1 组成数据第 0 页（Composition Data Page 0）

第 0 页提供设备的基本信息，所有 Mesh 设备都必须支持。它包含元素和模型组成、所支持的功能以及制造商信息。

<a id="composition-data-page-1"></a>

#### 67.1.7.2 组成数据第 1 页（Composition Data Page 1）

第 1 页提供模型间的关系信息，所有 Mesh 设备都必须支持。模型可以扩展一个或多个模型，也可与一个或多个模型对应。扩展通过 [`bt_mesh_model_extend()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf6356f715c8968151b8d539f2dd1880c) 建立，对应关系通过 [`bt_mesh_model_correspond()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga03ce9f6f9ccf734ea72beede09288923) 建立。[`CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_MODEL_EXTENSION_LIST_SIZE) 指定设备组成数据可保存的模型关系数量，应反映 `bt_mesh_model_extend()` 与 `bt_mesh_model_correspond()` 的调用数量。 相关链接：[`bt_mesh_model_extend()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#gaf6356f715c8968151b8d539f2dd1880c)；[`bt_mesh_model_correspond()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga03ce9f6f9ccf734ea72beede09288923)。

<a id="composition-data-page-2"></a>

#### 67.1.7.3 组成数据第 2 页（Composition Data Page 2）

第 2 页提供所支持的 Mesh 配置文件（mesh profile）信息。Mesh 配置文件规范为希望支持特定 Bluetooth SIG 配置文件的设备定义产品要求。当前支持的配置文件见 [Bluetooth SIG Assigned Numbers](https://www.bluetooth.com/specifications/assigned-numbers/uri-scheme-name-string-mapping/) 第 3.12 节。只有声明支持一个或多个 Mesh 配置文件的设备才必须支持第 2 页。

<a id="composition-data-pages-128-129-and-130"></a>

#### 67.1.7.4 组成数据第 128、129、130 页（Composition Data Pages 128, 129 and 130）

第 128、129、130 页分别映射第 0、1、2 页。当固件更新后组成数据将发生变化时，用这些页表示对应页面的新内容。详情见[组成数据与模型元数据（Composition Data and Models Metadata）](P104_Mesh固件更新服务端.md#bluetooth-mesh-dfu-srv-comp-data-and-models-metadata)。

<a id="delayable-messages"></a>

### 67.1.8 可延迟消息（Delayable messages）

可延迟消息功能通过 Kconfig 选项 [`CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_ACCESS_DELAYABLE_MSG) 启用。这是可选功能，实现规范对模型收到消息后发送的响应消息（response message）的建议。

响应消息应采用以下随机延迟：

- 收到的消息发往单播地址时，延迟 20—50 毫秒。

- 收到的消息发往组地址或虚拟地址时，延迟 20—500 毫秒。

设置 [`bt_mesh_msg_ctx.rnd_delay`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__msg__ctx.html#acb5b5de55f35b37ba4f34ffc08943184) 标志后触发可延迟消息功能；等待随机延迟到期期间，消息保存在本地内存中。

随机延迟到期时，若传输层内存不足以发送消息，则再推迟 10 毫秒。如果传输层因其他原因无法发送，可延迟消息功能会调用 [`bt_mesh_send_cb.start`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__send__cb.html#a2f84ef4cb2d28729cd98b844a3d25f55) 回调，并传入传输层错误码。

可延迟消息功能找不到足够空闲内存来保存新到来的消息时，会先发送那些延迟接近到期的消息，以释放内存。

Mesh 协议栈挂起或重置时，尚未发送的消息会被移除，并调用 [`bt_mesh_send_cb.start`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__send__cb.html#a2f84ef4cb2d28729cd98b844a3d25f55) 回调报告错误码。

注意（Note）

模型连续发送多条消息时，实际发送顺序可能与传给访问层的顺序不同，因为各消息可能具有不同的延迟。

同一模型发出的一组消息必须按特定顺序发送时，应把 [`bt_mesh_msg_ctx.rnd_delay`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__msg__ctx.html#acb5b5de55f35b37ba4f34ffc08943184) 设为 `false`，禁用随机化。

<a id="delayable-publications"></a>

### 67.1.9 可延迟发布（Delayable publications）

可延迟发布功能在以下场景实现规范建议的消息发布延迟：

- Bluetooth Mesh 协议栈启动时，或调用 [`bt_mesh_model_publish()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html#ga06644f8a5fa43351328d3f3403dbad03) 触发发布时，延迟 20—500 毫秒。

- 周期发布的消息延迟 20—50 毫秒。

此功能可选，通过 Kconfig 选项 [`CONFIG_BT_MESH_DELAYABLE_PUBLICATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_DELAYABLE_PUBLICATION) 启用。启用后，各模型可分别将 [`bt_mesh_model_pub.delayable`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__model__pub.html#a23a865dbd2dce5c1af074097864611e9) 位字段设为 `1` 或 `0`，开启或关闭可延迟发布。此位字段可随时修改。

<a id="api-reference"></a>

## 67.2 API 参考（API reference）

[访问层（Access layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__access.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/access.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/access.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/access.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh核心](P066_Mesh核心.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh模型](P068_Mesh模型.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P066_Mesh核心.md) · [返回大纲](大纲.md) · [下一章](P068_Mesh模型.md)

</details>

<!-- reading-navigation:end -->

---
id: learning.zephyr-docs.bluetooth.page-91
title: Mesh远程配网服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/rpr_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="remote-provisioning-server"></a>

<a id="bluetooth-mesh-models-rpr-srv"></a>

# 第91章\_远程配网服务端（Remote Provisioning Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/rpr_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：本页三段是应用集成片段，不是终端命令。Kconfig 片段放入应用配置；模型数组属于应用 C 源码；启用承载的调用则发生在有效 Mesh 运行环境中。它们与普通 PB-GATT 配网的支持范围不能混为一谈。

远程配网服务端是 Bluetooth Mesh 规范定义的基础模型，通过 [`CONFIG_BT_MESH_RPR_SRV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPR_SRV) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，用于支持设备远程加入 Mesh 网络。

远程配网服务端不提供独立控制 API，由远程配网客户端控制；它仅接受用本节点设备密钥加密的消息。 相关链接：[远程配网客户端（Remote Provisioning Client）](P090_Mesh远程配网客户端.md#bluetooth-mesh-models-rpr-cli)。

若存在远程配网服务端模型，必须在主元素上实例化。

经节点配网协议接口（NPPI）过程刷新设备密钥、节点地址或组成数据后，会触发 [`bt_mesh_prov.reprovisioned`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html#ac131476cdeb002f0027407b4cf80c2b5) 回调，详情见远程配网客户端章节。 相关链接：[远程配网客户端（Remote Provisioning Client）](P090_Mesh远程配网客户端.md#bluetooth-mesh-models-rpr-cli)。

<a id="how-to-integrate-the-model-into-an-application"></a>

## 91.1 如何将模型集成到应用（How to integrate the model into an application）

要在应用中添加远程配网服务端模型，请执行以下步骤：

- 在工程配置中启用以下 Kconfig 选项：

```ini
CONFIG_BT_MESH_RPR_SRV=y
```

> 译注——代码说明：这行 Kconfig 配置启用远程配网服务端支持；它是工程配置内容，不在终端执行，也不替代下一个片段的模型实例声明。

- 用 [`BT_MESH_MODEL_RPR_SRV`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__srv.html#ga49c08c3e98b0c3863dd79b37aea25b34) 宏，把模型实例加入主元素的模型列表 [`bt_mesh_elem.models`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__elem.html#a57fefe57d9425d6666495d1f72a3f132)，例如：

```c
static const struct bt_mesh_model models[] = {
        BT_MESH_MODEL_CFG_SRV,
        BT_MESH_MODEL_HEALTH_SRV(&health_srv, &health_pub),
        BT_MESH_MODEL_RPR_SRV,
        /* ... */
};

static const struct bt_mesh_elem elements[] = {
        BT_MESH_ELEM(0, models, BT_MESH_MODEL_NONE),
};
```

> 译注——代码说明：主元素的模型数组包含配置服务端、健康服务端和远程配网服务端。`health_srv`、`health_pub` 由应用提供；`/* ... */` 是原文省略的其他模型位置，不能据此认定整份应用已完整。结构和宏来自 Zephyr，应用声明的是实例。

- 调用 [`bt_mesh_prov_enable()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga6c8dc1b09d4cde8738be83c992b860a9) 并传入 [`BT_MESH_PROV_REMOTE`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ggaa157eb0fee30c28092a11993872b8fdda4222d03b09ba43b6ea772738b8987501)，启用远程配网承载（PB-Remote）：

```c
err = bt_mesh_prov_enable(BT_MESH_PROV_REMOTE);
if (err) {
        printk("PB-Remote enable failed (err %d)\n", err);
}
```

> 译注——代码说明：调用为当前节点启用 PB-Remote，`err` 应由所在函数定义并检查；输出 PB-Remote enable failed 表示启用失败。后续客户端控制只能在前置初始化和启用成功后进行。

<a id="limitations"></a>

## 91.2 限制（Limitations）

远程配网服务端模型有以下限制：

- 不支持通过 PB-GATT 为未配网设备配网。

- 支持全部 NPPI 过程。但如果设备固件更新后组成数据发生变化，见[固件影响（firmware effect）](P102_Mesh设备固件更新.md#bluetooth-mesh-dfu-firmware-effect)，设备无法继续保持已配网状态。预计组成数据会变化时，应使设备退出已配网状态。

<a id="api-reference"></a>

### 91.2.1 API 参考（API reference）

[远程配网服务端（Remote provisioning server）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/rpr_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/rpr_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/rpr_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh远程配网客户端](P090_Mesh远程配网客户端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh子网桥接](P092_Mesh子网桥接.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P090_Mesh远程配网客户端.md) · [返回大纲](大纲.md) · [下一章](P092_Mesh子网桥接.md)

</details>

<!-- reading-navigation:end -->

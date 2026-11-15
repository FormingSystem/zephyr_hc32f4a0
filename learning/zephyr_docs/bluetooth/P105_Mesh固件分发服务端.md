---
id: learning.zephyr-docs.bluetooth.page-105
title: Mesh固件分发服务端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/dfd_srv.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="firmware-distribution-server"></a>

<a id="bluetooth-mesh-dfd-srv"></a>

# 第105章\_固件分发服务端（Firmware Distribution Server）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/dfd_srv.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

固件分发服务端（Firmware Distribution Server）模型实现设备固件更新（DFU）子系统的分发器角色。它扩展大对象传输服务端，接收来自发起器节点的固件二进制映像；同时实例化固件更新客户端，利用它向整个 Mesh 网络分发更新。 相关链接：[设备固件更新（Device Firmware Update，DFU）](P102_Mesh设备固件更新.md#bluetooth-mesh-dfu)；[大对象传输服务端（BLOB Transfer Server）](P100_Mesh大对象传输服务端.md#bluetooth-mesh-blob-srv)；[固件更新客户端（Firmware Update Client）](P103_Mesh固件更新客户端.md#bluetooth-mesh-dfu-cli)。

注意（Note）

目前，固件分发服务端仅支持通过 SMP 服务带外获取（Out-of-band retrieval，OOB）固件映像。

> 译注——带外上传依据：正文按官方页面保留 SMP（Simple Management Protocol，简单管理协议）的限制表述。本次读取的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/mesh/dfd_srv.h)包含 `CONFIG_BT_MESH_DFD_SRV_OOB_UPLOAD`、`BT_MESH_DFD_SRV_OOB_INIT` 和应用回调 `start_oob_upload`、`cancel_oob_upload`、`oob_progress_get`；[官方实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/dfd_srv.c)按配置分支处理上传。该证据表明 OOB 上传具有配置与应用接入前提，不表示已在本仓库实测，也不能据此推断任意 URI 方案都可用。本仓库相对源码：[dfd_srv.h](../../../include/zephyr/bluetooth/mesh/dfd_srv.h)、[dfd_srv.c](../../../subsys/bluetooth/mesh/dfd_srv.c)。

固件分发服务端没有独立的操作 API，而是依靠另一设备上的固件分发客户端（Firmware Distribution Client）模型提供信息，并触发映像分发和上传。

> 译注——API 的含义：这里指常规上传／分发控制由远端模型消息驱动；并非头文件没有公开类型、初始化宏或 OOB 完成通知函数。应结合上面的源码接口理解这一表述。

<a id="firmware-slots"></a>

## 105.1 固件槽（Firmware slots）

固件分发服务端可以存储多个待分发映像。每个槽保存一个独立映像及其元数据，可以按任意顺序分发给网络中的其他 Mesh 节点。映像内容、格式和大小由厂商定义，也可能包含其他厂商的数据。应用不应尝试执行或修改这些映像。

固件分发客户端远程管理这些槽，可以上传新槽，也可以删除旧槽。应用通过服务端回调 `bt_mesh_fd_srv_cb` 得知槽的变化。每个槽的元数据由内部保存，但应用必须提供读取和写入固件映像所用的[大对象流（BLOB streams）](P098_Mesh大对象传输.md#bluetooth-mesh-blob-stream)。

> 译注——回调类型拼写：原页写作 `bt_mesh_fd_srv_cb`；本次官方头文件实际声明的是 `struct bt_mesh_dfd_srv_cb`，中间为 `dfd`。译文保留原标识并在此注明，避免直接复制旧拼写。

<a id="api-reference"></a>

## 105.2 API 参考（API reference）

[固件分发服务端模型（Firmware Distribution Server model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__dfd__srv.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/dfd_srv.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/dfd_srv.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/dfd_srv.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh固件更新服务端](P104_Mesh固件更新服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh_Shell](P106_Mesh_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P104_Mesh固件更新服务端.md) · [返回大纲](大纲.md) · [下一章](P106_Mesh_Shell.md)

</details>

<!-- reading-navigation:end -->

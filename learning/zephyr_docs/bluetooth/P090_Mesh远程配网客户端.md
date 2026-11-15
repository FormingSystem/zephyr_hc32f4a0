---
id: learning.zephyr-docs.bluetooth.page-90
title: Mesh远程配网客户端
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/rpr_cli.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="remote-provisioning-client"></a>

<a id="bluetooth-mesh-models-rpr-cli"></a>

# 第90章\_远程配网客户端（Remote Provisioning Client）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/rpr_cli.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读定位：远程配网（Remote Provisioning）通过已经加入网络的服务端节点，在服务端附近发现并加入新设备。示例地址、UUID 和网络索引均为占位场景，应用必须使用实际扫描结果和已管理的地址空间。

远程配网客户端是 Bluetooth Mesh 规范定义的基础模型，通过 [`CONFIG_BT_MESH_RPR_CLI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_MESH_RPR_CLI) 启用。

该模型在《Bluetooth Mesh Protocol Specification》1.1 版引入，通过与支持远程配网服务端的节点交互，把设备远程加入 Mesh 网络，并执行节点配网协议接口（Node Provisioning Protocol Interface，NPPI）过程。 相关链接：[远程配网服务端（Remote Provisioning Server）](P091_Mesh远程配网服务端.md#bluetooth-mesh-models-rpr-srv)。

远程配网客户端使用目标服务端实例所在节点的设备密钥，与远程配网服务端通信。

若存在远程配网客户端模型，必须在主元素上实例化。

<a id="scanning"></a>

## 90.1 扫描（Scanning）

扫描过程用于发现远程配网服务端附近的未配网设备。客户端调用 [`bt_mesh_rpr_scan_start()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#gaf404922f2340442490f1ab29191f43e3) 启动扫描：

```c
static void rpr_scan_report(struct bt_mesh_rpr_cli *cli,
            const struct bt_mesh_rpr_node *srv,
            struct bt_mesh_rpr_unprov *unprov,
            struct net_buf_simple *adv_data)
{

}

struct bt_mesh_rpr_cli rpr_cli = {
   .scan_report = rpr_scan_report,
};

const struct bt_mesh_rpr_node srv = {
   .addr = 0x0004,
   .net_idx = 0,
   .ttl = BT_MESH_TTL_DEFAULT,
};

struct bt_mesh_rpr_scan_status status;
uint8_t *uuid = NULL;
uint8_t timeout = 10;
uint8_t max_devs = 3;

bt_mesh_rpr_scan_start(&rpr_cli, &srv, uuid, timeout, max_devs, &status);
```

> 译注——代码说明：此段定义扫描报告回调、客户端实例和目标服务端参数：服务端地址 0x0004、网络索引 0、默认 TTL，扫描 10 秒且最多报告 3 台设备。`uuid = NULL` 表示不限定某个 UUID；回调体为空，需要应用实际处理结果。返回值与 `status` 应分别检查；调用返回不能代替后续扫描报告处理。参数单位及回调字段可对照[官方 rpr_cli.h](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/mesh/rpr_cli.h)。

上述伪代码在目标远程配网服务端节点上启动扫描，持续十秒，扫描多个设备，生成的报告最多包含三台未配网设备。若指定 UUID 参数，则仅扫描相应 UUID 的设备。过程完成后，服务端发送扫描报告，由客户端的 [`bt_mesh_rpr_cli.scan_report`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__rpr__cli.html#a32b3c63218b506d1bc5759640cb3fb81) 回调处理。

客户端还支持通过 [`bt_mesh_rpr_scan_start_ext()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html#ga934104e6ee33ba8c228fde4c68e752e1) 扩展扫描，允许服务端报告特定设备的附加数据，补充普通扫描结果。若未配网设备支持，服务端会采用主动扫描向其请求扫描响应。

<a id="provisioning"></a>

## 90.2 配网（Provisioning）

远程配网客户端通过 [`bt_mesh_provision_remote()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#ga9fc414e4e15d6b3ab0dae5483ed62982) 启动配网过程：

```c
struct bt_mesh_rpr_cli rpr_cli;

const struct bt_mesh_rpr_node srv = {
   .addr = 0x0004,
   .net_idx = 0,
   .ttl = BT_MESH_TTL_DEFAULT,
};

uint8_t uuid[16] = { 0xaa };
uint16_t addr = 0x0006;
uint16_t net_idx = 0;

bt_mesh_provision_remote(&rpr_cli, &srv, uuid, net_idx, addr);
```

> 译注——代码说明：此段的服务端仍是地址 0x0004；待加入设备使用示例 UUID，主元素拟分配 0x0006，使用索引 0 的网络密钥。`{ 0xaa }` 仅初始化 UUID 首字节为 0xaa，其余为零，不是每个字节都为 0xaa。片段省略了模型集成、实例初始化及错误处理，应按实际应用补齐。

上述伪代码经远程配网服务端节点为设备配网，尝试加入相应 UUID 的设备，使用索引为零的网络密钥，并给其主元素分配地址 0x0006。

注意（Note）

远程配网期间会触发与普通配网相同的 [`bt_mesh_prov`](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__prov.html) 回调，详情见配网章节。 相关链接：[配网（Provisioning）](P070_Mesh配网.md#bluetooth-mesh-provisioning)。

<a id="re-provisioning"></a>

## 90.3 重新配网（Re-provisioning）

除扫描和配网外，远程配网客户端还可重新配置支持远程配网服务端的设备的节点地址、设备密钥和组成数据。该功能通过节点配网协议接口（NPPI）提供，支持以下三种过程： 相关链接：[远程配网服务端（Remote Provisioning Server）](P091_Mesh远程配网服务端.md#bluetooth-mesh-models-rpr-srv)。

- 设备密钥刷新（Device Key Refresh）：改变目标节点的设备密钥，无须重新配置节点。

- 节点地址刷新（Node Address Refresh）：改变节点的设备密钥和单播地址。

- 节点组成刷新（Node Composition Refresh）：改变节点设备密钥，并添加或删除模型或功能。

三种 NPPI 过程均可通过 [`bt_mesh_reprovision_remote()`](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__prov.html#gaa02583390f635ac251d22ed9ff953974) 发起：

```c
struct bt_mesh_rpr_cli rpr_cli;
struct bt_mesh_rpr_node srv = {
   .addr = 0x0006,
   .net_idx = 0,
   .ttl = BT_MESH_TTL_DEFAULT,
};

bool composition_changed = false;
uint16_t new_addr = 0x0009;

bt_mesh_reprovision_remote(&rpr_cli, &srv, new_addr, composition_changed);
```

> 译注——代码说明：此段目标已经是地址 0x0006 的已配网节点，拟改为 0x0009，`composition_changed = false` 表示示例没有声明组成数据变化。按正文给出的地址与标志组合选择 NPPI 过程，并在应用回调中确认最终结果；不能仅改本地地址变量就认为远端刷新成功。

上述伪代码触发目标节点的节点地址刷新。具体过程不是直接指定，而由其他输入参数决定：例中当前单播地址为 0x0006，新地址为 0x0009。若两地址相同且 `composition_changed` 为 true，则触发节点组成刷新；若两地址相同且 `composition_changed` 为 false，则触发设备密钥刷新。

<a id="api-reference"></a>

## 90.4 API 参考（API reference）

[远程配网客户端模型（Remote Provisioning Client model）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__rpr__cli.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/rpr_cli.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/rpr_cli.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/rpr_cli.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh操作码聚合器服务端](P089_Mesh操作码聚合器服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh远程配网服务端](P091_Mesh远程配网服务端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P089_Mesh操作码聚合器服务端.md) · [返回大纲](大纲.md) · [下一章](P091_Mesh远程配网服务端.md)

</details>

<!-- reading-navigation:end -->

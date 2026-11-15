---
id: learning.zephyr-docs.firmware_update.mgmtex-hawkbit
title: hawkBit升级示例
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/mgmt/hawkbit/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="hawkbit-api"></a>

# 第24章\_hawkBit升级示例

原文：[Eclipse hawkBit Direct Device Integration API](https://docs.zephyrproject.org/latest/samples/subsys/mgmt/hawkbit/README.html)。读取日期：2026-10-13，`latest`。

## 24.1\_hawkBit设备集成

Eclipse hawkBit升级服务器提供 **表述性状态转移（Representational State Transfer，REST）**资源，设备借此获取软件更新任务。**直接设备集成（Direct Device Integration，DDI）**的 **应用程序编程接口（Application Programming Interface，API）**基于 **超文本传输协议（Hypertext Transfer Protocol，HTTP）**和轮询机制。

示例支持 **轮询模式（Polling Mode）**与 **手动模式（Manual Mode）**。轮询按预定周期检查并安装更新，无需人工介入；手动模式由使用者触发服务器查询，发现更新后安装。原文将两种实现称为 `hawkbit_polling` 和 `hawkbit_manual`，示例代码见[官方应用源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/mgmt/hawkbit/src/main.c)。

## 24.2\_平台与引导要求

默认目标是[STM32H573I-DK](https://docs.zephyrproject.org/latest/boards/st/stm32h573i_dk/doc/index.html#stm32h573i_dk)，板卡标识 `stm32h573i_dk`。具备互联网连接的其他平台原则上可构建运行，但可能需要适配。

**蓝牙低功耗（Bluetooth Low Energy）**、**低功耗无线个域网IPv6适配（IPv6 over Low-Power Wireless Personal Area Networks，6LoWPAN）**、802.15.4和OpenThread连接需要额外配置片段；许多此类连接还需要边缘网关或 **边界路由器（Border Router）**。原例要求MCUboot **引导加载程序（Bootloader）**，背景见[设备固件升级](P002_设备固件升级.md)。

## 24.3\_启动服务器与认证配置

默认网页界面端口8088，设备DDI API端口8080，均使用HTTP。主机上的原命令为：

```shell
git clone https://github.com/eclipse-hawkbit/hawkbit.git
cd hawkbit/docker/postgres
docker compose -fdocker-compose-monolith-dbinit-with-ui-postgres.yml up -d
```

打开服务器地址 `<your-ip-address>:8088`，默认用户名和密码均为示例值 `admin`。在左侧 **配置（Config）**页，将 `authentication.gatewaytoken.key` 设为示例令牌 `abcd1234`，并启用 `authentication.gatewaytoken.enabled`。

服务器令牌必须与Kconfig配置项 [`CONFIG_HAWKBIT_DDI_SECURITY_TOKEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_DDI_SECURITY_TOKEN) 相同。若启用了 [`CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME)，可在设备运行时设置令牌，仍须保持两端一致。这些默认账号与令牌用于复现原示例。

## 24.4\_构建与烧录

从Zephyr源码目录使用west和 **系统构建（System Build，sysbuild）**：

```shell
west build -b stm32h573i_dk --sysbuild samples/subsys/mgmt/hawkbit
```

要在运行时设置服务器地址和端口，在应用 `prj.conf` 启用Kconfig配置项 [`CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME)。构建系统自动使用MCUboot仓库中的 `root-rsa-2048.pem` 签名。

> 译注：该文件是公开开发密钥，不适合保护实际部署。密钥的路径解析和替换方法见[镜像签名](P005_镜像签名.md)，不能因构建成功就认为使用了独有密钥。

通过sysbuild同时构建后，一条命令烧录引导程序与应用：

```shell
west flash
```

启动后应用输出构建时间；联网后应能在服务器 **目标（Targets）**页看到以板卡名开头的目标。

## 24.5\_上传测试镜像与分配

原文这一步使用构建目录里的 `zephyr.signed.bin`。准备好新的测试构建后，在服务器界面按以下流程操作：

1. 打开 **软件模块（Software Modules）**，点击加号；类型选择 **应用（Application）**，填写名称和版本，可按测试需要设置。
2. 启用 **创建单软件模块分发集（Create single software module distribution set）**，将 **分发集类型（Distribution Set Type）**设为 **仅应用（App(s) only）**。Zephyr场景里软件模块与分发集为一对一关系。
3. 点击 **创建（Create）**，在制品上传对话框选择 `zephyr.signed.bin`，再点 **完成（Finish）**。
4. 回到Targets，选中对应开发板，点击夹子形图标分配分发集，选择新建条目，再点 **分配（Assign）**。

> 译注：此步骤原文没有再次列构建命令。若希望重启后构建时间不同，必须实际形成新的固件构建；只改变服务器端名称或版本标签不会改变固件内部内容。

## 24.6\_执行与确认结果

在设备调试终端，可以等待客户端自动查询（原文默认为每5分钟）、重启设备，或输入：

```shell
hawkbit run
```

设备会查询服务器并下载已分配更新；成功时输出 `Update installed`（更新已安装），然后自动重启运行新镜像。重启后显示新的构建时间，再次查询应输出 `Image is already updated`（镜像已经是最新状态）。

更多接口见[hawkBit空中升级API](P027_hawkBit接口.md)与[JavaScript对象表示法（JavaScript Object Notation，JSON）处理API](https://docs.zephyrproject.org/latest/doxygen/html/group__json.html)。

[上一章：HTTP固件升级示例](P023_HTTP固件升级示例.md) · [下一章：UpdateHub升级示例](P025_UpdateHub升级示例.md) · [返回大纲](大纲.md)

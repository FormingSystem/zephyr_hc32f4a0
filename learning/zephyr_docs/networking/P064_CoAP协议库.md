---
id: learning.zephyr-docs.networking.page-64
title: CoAP协议库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/coap.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_CoAP协议库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/coap.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 64.1 概览（Overview）

受限应用协议（Constrained Application Protocol，CoAP）是一种专门面向受限节点和受限网络的 Web 传输协议，例如低功耗、有损网络。它为支持 CoAP 特性的 REST 风格 Web 服务（RESTful Web Services）提供方便的接口。协议本身见[RFC 7252](https://datatracker.ietf.org/doc/html/rfc7252.html)。

Zephyr 提供同时支持客户端（Client）和服务器（Server）角色的 CoAP 库，通过 [`CONFIG_COAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP) 启用，并可按需求配置。基础库使用普通缓冲区（Buffer）处理报文：应用自行创建通信套接字（Socket），把缓冲区交给库进行解析等操作；库本身不替应用创建套接字。

在 CoAP 之上，Zephyr 还支持轻量级机器间通信（Lightweight Machine-to-Machine，LwM2M）协议，提供简单、低成本的远程管理和服务启用机制。详见[LwM2M 指南](P073_LwM2M协议栈.md#lwm2m-interface)。

| 支持的规范 | 主题 |
| --- | --- |
| [RFC 7252](https://datatracker.ietf.org/doc/html/rfc7252.html) | 受限应用协议（CoAP） |
| [RFC 6690](https://datatracker.ietf.org/doc/html/rfc6690.html) | 受限 REST 环境（Constrained RESTful Environments，CoRE）链接格式 |
| [RFC 7959](https://datatracker.ietf.org/doc/html/rfc7959.html) | CoAP 分块传输（Block-Wise Transfer） |
| [RFC 7641](https://datatracker.ietf.org/doc/html/rfc7641.html) | CoAP 资源观察（Observing Resources） |
| [RFC 8613](https://datatracker.ietf.org/doc/html/rfc8613.html) | 受限 REST 环境对象安全（Object Security for Constrained RESTful Environments，OSCORE） |

注意：并非这些 RFC 的所有部分都已实现，功能支持取决于 Zephyr 的需求。OSCORE 的具体用法见[OSCORE 支持说明](P067_CoAP_OSCORE对象安全.md#coap-oscore-interface)。

## 64.2 自定义服务器（CoAP Server）

Zephyr 已有[CoAP 服务器子系统](P066_CoAP服务器库.md#coap-server-interface)。本节说明直接使用基础库实现自定义服务器的方式。

先定义服务器资源（Resource）。`.well-known/core` 应放在所有需要出现在其发现响应中的资源之前：

```c
static struct coap_resource resources[] = {
    { .get = well_known_core_get,
      .path = COAP_WELL_KNOWN_CORE_PATH,
    },
    { .get  = sample_get,
      .post = sample_post,
      .del  = sample_del,
      .put  = sample_put,
      .path = sample_path
    },
    { },
};
```

应用从套接字读取数据，将缓冲区交给库解析。报文有效时，使用解析结果及上述资源表调用对应的请求回调；回调负责回复客户端或执行请求所要求的动作：

```c
coap_packet_parse(&request, data, data_len, options, opt_num);
...
coap_handle_request(&request, resources, options, opt_num,
                    client_addr, client_addr_len);
```

启用 [`CONFIG_COAP_URI_WILDCARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_URI_WILDCARD) 后，资源路径可以使用类似 MQTT 的通配符（Wildcard）：`+` 匹配单层路径，`#` 匹配多层路径。

```c
static const char * const led_set[] = { "led","+","set", NULL };
static const char * const btn_get[] = { "button","#", NULL };
static const char * const no_wc[] = { "test","+1", NULL };
```

上例接受 `/led/0/set`、`led/1234/set`、`led/any/set`、`/button/door/1`、`/test/+1`；对于 `/led/1`、`/test/21`、`/test/1`，返回 `-ENOENT`。这里 `+1` 是普通路径内容，不是单独的 `+` 通配符。

这个选项默认启用。如果资源名本身包含 `/some_resource/+/#` 这样的字符组合，应禁用通配符功能，避免意外匹配。

## 64.3 自定义客户端（CoAP Client）

Zephyr 也已有[CoAP 客户端子系统](P065_CoAP客户端库.md#coap-client-interface)。本节是直接使用基础库构造请求的示例。

客户端已知服务器资源时，可以准备请求并等待响应；尚不知道资源时，可请求 `.well-known/core` 获取资源信息：

```c
/* Initialize the CoAP message */
char *path = "test";
struct coap_packet request;
uint8_t data[100];
uint8_t payload[20];

coap_packet_init(&request, data, sizeof(data),
                 1, COAP_TYPE_CON, 8, coap_next_token(),
                 COAP_METHOD_GET, coap_next_id());

/* Append options */
coap_packet_append_option(&request, COAP_OPTION_URI_PATH,
                          path, strlen(path));

/* Append Payload marker if you are going to add payload */
coap_packet_append_payload_marker(&request);

/* Append payload */
coap_packet_append_payload(&request, (uint8_t *)payload,
                           sizeof(payload) - 1);

/* send over sockets */
```

> 译注：这是报文组装片段，最后的套接字发送尚未展开。`payload` 在片段中只是声明，实际使用前必须填写有效内容；各初始化、选项和负载追加操作的返回值也应检查。不要把未初始化的缓冲区当作测试数据发送。

## 64.4 使用 libcoap 测试（Testing）

[libcoap](https://github.com/obgm/libcoap) 面向算力、无线覆盖范围、内存、带宽或分组尺寸受限的设备实现轻量级应用协议。其 `examples/etsi_coaptest.sh` 脚本可测试 Zephyr CoAP 服务器功能；配套说明见[net-tools](https://github.com/zephyrproject-rtos/net-tools)。

按[QEMU 联网指南](P009_QEMU联网概览.md#networking-with-qemu)构建并运行[CoAP 服务示例](P072_CoAP服务示例.md#coap-server)后，在 Linux 主机、包含 [`libcoap`](#libcoap) 源码子目录的位置执行以下 ETSI（欧洲电信标准协会，European Telecommunications Standards Institute）测试命令：

```shell
sudo ./libcoap/examples/etsi_coaptest.sh -i tap0 2001:db8::1
```

`tap0` 和 `2001:db8::1` 应对应实际测试接口与服务器地址。

## 64.5 使用 TTCN3 测试

Eclipse 提供基于 TTCN3（Testing and Test Control Notation version 3，测试与测试控制表示法第三版）的 CoAP 测试。原文在 Linux 上安装 `eclipse-titan`，并为 TITAN 工具设置链接：

```shell
sudo apt-get install eclipse-titan

cd /usr/share/titan

sudo ln -s /usr/bin bin
sudo ln /usr/bin/titanver bin
sudo ln -s /usr/bin/mctr_cli bin
sudo ln -s /usr/include/titan include
sudo ln -s /usr/lib/titan lib

export TTCN3_DIR=/usr/share/titan

git clone https://gitlab.eclipse.org/eclipse/titan/titan.misc.git

cd titan.misc
```

> 译注：`/usr/share/titan`、`/usr/bin`、`/usr/include/titan`、`/usr/lib/titan` 是原文的 Linux 系统安装位置，不是本仓库的固定存放位置。原命令中 `ln` 和 `ln -s` 分别创建硬链接、符号链接；若发行版已提供相应布局，不应重复创建。原例切入系统目录后仍在其中克隆，普通用户可能没有写权限；实际可在读者有写权限的工作目录克隆 `titan.misc`，并保持 `TTCN3_DIR` 指向已核实的 TITAN 安装目录。本轮未安装或改动这些系统路径。

按下面两处官方说明配置 CoAP 测试套件：

- [TITAN misc 项目](https://gitlab.eclipse.org/eclipse/titan/titan.misc)。
- [CoAP_Conf 测试套件](https://gitlab.eclipse.org/eclipse/titan/titan.misc/-/tree/master/CoAP_Conf)。

测试套件构建完成后，按[QEMU 联网指南](P009_QEMU联网概览.md#networking-with-qemu)运行[CoAP 服务示例](P072_CoAP服务示例.md#coap-server)。根据实际网络修改 `coap.cfg` 中客户端（测试套件）与服务器（Zephyr 示例）的地址，然后在包含测试程序和配置的位置执行：

```shell
ttcn3_start coaptests coap.cfg
```

原文测试输出如下：

```text
Verdict statistics: 0 none (0.00 %), 10 pass (100.00 %), 0 inconc (0.00 %), 0 fail (0.00 %), 0 error (0.00 %).
Test execution summary: 10 test cases were executed. Overall verdict: pass
```

这里的 10 项通过是官方原页记录，不是本轮执行结果。

## 64.6 API 与相关示例（API Reference）

详细接口见[CoAP 库 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html)，其翻译状态独立跟踪。

| 官方示例 | 作用 |
| --- | --- |
| [CoAP 客户端](P068_CoAP客户端示例.md) | 使用基础库获取资源 |
| [CoAP 下载](P070_CoAP下载示例.md#coap-download) | 使用客户端 API 通过 GET 下载数据 |
| [CoAP 服务](P072_CoAP服务示例.md#coap-server) | 在服务器子系统中注册资源 |
| [CoAP TCP 客户端](P069_CoAP_TCP客户端示例.md#coap-client-tcp) | 通过 TCP 与服务器通信 |
| [CoAP 上传](P071_CoAP上传示例.md#coap-upload) | 使用客户端 API 通过 PUT 上传数据 |


<a id="coap"></a>
<a id="coap-sock-interface"></a>
<a id="contents"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="id7"></a>
<a id="id8"></a>
<a id="id9"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="index-1"></a>
<a id="index-2"></a>
<a id="index-3"></a>
<a id="index-4"></a>
<a id="index-5"></a>
<a id="index-6"></a>
<a id="sample-usage"></a>
<a id="coap-server"></a>
<a id="coap-client"></a>
<a id="testing"></a>
<a id="libcoap"></a>
<a id="ttcn3"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：MQTT_SN客户端库](P062_MQTT_SN客户端库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：CoAP客户端库](P065_CoAP客户端库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P063_MQTT_SN发布者示例.md) · [返回大纲](大纲.md) · [下一章](P065_CoAP客户端库.md)

</details>

<!-- reading-navigation:end -->

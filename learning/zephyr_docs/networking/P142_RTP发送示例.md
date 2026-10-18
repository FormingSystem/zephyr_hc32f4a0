---
id: learning.zephyr-docs.networking.page-142
title: RTP发送示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/rtp/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第142章\_RTP发送示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/rtp/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

本示例展示通过 UDP 组播套接字（UDP Multicast Socket）使用 Zephyr 实时传输协议（Real-time Transport Protocol，RTP）API 发送和接收音频流。

构建时用附加配置文件选择角色：`source.conf` 对应发送源（Source），`sink.conf` 对应接收端（Sink）。两端共用组播地址 `239.0.1.1` 和端口 `5004`。加入 `ipv6.conf` 时，会话改用 IPv6 组播地址 `ff02::5004`，端口保持不变。

发送源通过载荷类型（Payload Type）`97` 的 RTP 包发送 100 Hz 正弦波，格式为 16 位单声道、每秒 8000 个采样。每 50 ms 发送一次，每包包含 400 个采样，即正弦波的 5 个完整周期。

接收端加入组播组，通过回调 API 接收数据流。原文描述每 5 秒记录一次已收包数，并在 500 ms 内未收到包时记录超时警告。

可[在 GitHub 查看官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/rtp/README.rst/..)。

> 译注——日志和超时的实际触发：当前官方 [`src/main.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/rtp/src/main.c) 按收到的包数输出统计；源码条件在递增前计数为零时打印开始接收，之后在累计计数为 100 的倍数时打印数量。固定 50 ms 发包时，100 个包约对应 5 秒，但不是独立的 5 秒日志定时器。500 ms 超时工作在接收回调中重新安排，因此开始收到包后停止来包才会触发这条警告；它不是启动后未收到首包的独立倒计时。超时后计数会清零。

## 2. 前提条件（Requirements）

按[与主机系统联网](P007_与主机系统联网.md#networking-with-host)准备网络。

## 3. 在 native_sim 上运行（Running on native_sim）

在[原生模拟器 native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim) 上运行时，先按照主机联网文档建立 `zeth` TAP 接口。

与 FFmpeg 联调时，Linux 内核需要针对组播地址的显式路由，以便通过 `zeth` 而非默认网口传输数据。接口启用后，在 Linux 主机的 Bash 中执行：

```sh
sudo ip route add 239.0.1.1 dev zeth
```

> 译注——主机配置：该命令修改主机路由，执行目录不限，但 `zeth` 必须是已创建的实际测试接口。已有正确路由时不必重复添加；该命令针对 IPv4 地址，不等于同时完成 IPv6 链路本地组播的接口和路由准备。

## 4. 构建（Building）

### 4.1 发送源（Source）

原文构建命令：

```sh
west build -b <board to use> samples/net/rtp -- -DCONF_FILE=source.conf
```

### 4.2 接收端（Sink）

原文构建命令：

```sh
west build -b <board to use> samples/net/rtp -- -DCONF_FILE=sink.conf
```

> 译注——配置合并修正：上述命令及后续原文命令使用 `CONF_FILE`，但当前 [source.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/rtp/source.conf) 和 [sink.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/rtp/sink.conf) 只提供角色与少量参数，网络和 RTP 公共配置在 [prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/rtp/prj.conf)。官方 [tests.yaml](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/rtp/tests.yaml) 使用 `EXTRA_CONF_FILE` 在默认 `prj.conf` 后追加角色配置，示例 [CMakeLists.txt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/rtp/CMakeLists.txt) 没有替原文命令自动补回 `prj.conf`。实际复现宜沿用测试清单的追加方式；下面给出使用不同构建目录的对应命令，原命令仍保留供对照。

以下为译注补充命令。在已准备好 native_sim 构建环境的 Linux Bash 中，从 Zephyr 源码根目录执行。任选所需角色；两个目录由构建工具生成，便于避免角色配置混用：

```sh
# Linux Bash；当前位置为 Zephyr 源码根；前提是已具备 native_sim 构建环境。
# 发送源：保留默认 prj.conf，再追加 source.conf。
west build -b native_sim/native/64 -d build/rtp-source samples/net/rtp -- -DEXTRA_CONF_FILE=source.conf
# 接收端：保留默认 prj.conf，再追加 sink.conf。
west build -b native_sim/native/64 -d build/rtp-sink samples/net/rtp -- -DEXTRA_CONF_FILE=sink.conf
```

构建生成相应程序后，按主机联网文档启动所选角色。两台模拟设备同时使用时，需要按多实例联网方式准备各自接口，不能把“两份程序已编译”当作已经完成相互连通。

### 4.3 使用 net_pkt 的更快协议栈（Faster RTP Stack with net_pkt）

原文说明，`net_pkt.conf` 会调整网络包池以提高吞吐量，可与任一角色组合：

```sh
west build -b <board to use> samples/net/rtp -- -DCONF_FILE="source.conf net_pkt.conf"
west build -t run
```

```sh
west build -b <board to use> samples/net/rtp -- -DCONF_FILE="sink.conf net_pkt.conf"
west build -t run
```

> 译注——实际文件内容：当前官方 [net_pkt.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/rtp/net_pkt.conf) 只启用 [`CONFIG_RTP_TRANSPORT_NET_PKT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_TRANSPORT_NET_PKT) 并禁用 [`CONFIG_RTP_TRANSPORT_SOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_TRANSPORT_SOCKET)，并没有直接设置包池数量。它切换传输后端，不能照原文概括为修改了包池参数。配置合并仍应使用 `EXTRA_CONF_FILE`，例如在前述构建命令中把值设为 `"source.conf;net_pkt.conf"`；接收端则使用 `"sink.conf;net_pkt.conf"`。使用自定义构建目录时，运行命令也需要用 `-d` 指定相同目录。

### 4.4 使用 IPv6（Building with IPv6）

`ipv6.conf` 将 RTP 会话切换到 IPv6 组播地址 `ff02::5004`。它可以与任一角色组合，也可以再与 `net_pkt.conf` 组合：

```sh
west build -b <board to use> samples/net/rtp -- -DCONF_FILE="source.conf ipv6.conf"
west build -t run
```

```sh
west build -b <board to use> samples/net/rtp -- -DCONF_FILE="sink.conf ipv6.conf"
west build -t run
```

> 译注——组合方式：按上述修正，使用追加配置，例如 `EXTRA_CONF_FILE="source.conf;ipv6.conf"`，或 `EXTRA_CONF_FILE="sink.conf;net_pkt.conf;ipv6.conf"`。`<board to use>` 是原文板目标占位符，应换成实际目标；网络配置及 `run` 支持取决于目标环境。下方 FFmpeg 原例使用 IPv4，不会因 Zephyr 增加此配置文件而自动改成 IPv6 测试。

## 5. 使用 FFmpeg 测试（Testing with FFmpeg）

可使用 [FFmpeg](https://ffmpeg.org) 与任一角色联调。以下命令在安装了 FFmpeg、已准备测试接口和路由的 Linux 主机 Bash 中运行。

### 5.1 测试发送源（Testing the Source）

要用 FFmpeg 接收发送源的数据流，先在选定的测试目录创建 `stream.sdp`，用会话描述协议（Session Description Protocol，SDP）描述 RTP 会话：

```text
v=0
o=- 0 0 IN IP4 127.0.0.1
s=No Name
c=IN IP4 239.0.1.1
t=0 0
a=tool:libavformat 58.76.100
m=audio 5004 RTP/AVP 97
a=rtpmap:97 L16/8000/1
```

再从同一目录执行 FFmpeg，将收到的数据保存为 WAV 文件：

```sh
ffmpeg -protocol_whitelist file,udp,rtp -i stream.sdp \
       -acodec pcm_s16le -ar 8000 -ac 1 \
       -f wav out.wav
```

> 译注——输入和输出：`stream.sdp` 是读者按上文新建的配置文件，`out.wav` 是 FFmpeg 执行后产生的音频文件；官方页面没有提供需要下载的现成音频附件。SDP 的 `L16/8000/1` 声明线性 16 位 PCM、8000 Hz、单声道，并把动态载荷类型 `97` 映射到该格式。官方发送源先将样本转换为大端字节序后发送，输出 WAV 的 `pcm_s16le` 则指定本地文件的小端 PCM 编码。

### 5.2 测试接收端（Testing the Sink）

使用 FFmpeg 向接收端发送 8 kHz 单声道静音流，传输方式为 RTP 组播：

```sh
ffmpeg -re -f lavfi -i anullsrc=r=8000:cl=mono \
       -acodec pcm_s16le \
       -f rtp -rtp_flags latm \
       -pkt_size 1440 \
       rtp://239.0.1.1:5004
```

> 译注——测试含义：当前示例接收回调只统计包数和重新安排超时，并不播放音频，也不校验或解码音频载荷。原命令指定 `pcm_s16le`，不能因收包日志出现就认为它验证了与发送源 `L16` 描述完全相同的音频格式。这里保留原命令，用它观察收包和超时行为；具体编解码互通仍需按双方载荷约定另行验证。

## 6. 示例输出（Sample Output）

### 6.1 发送源（Source）

```text
*** Booting Zephyr OS build v4.4.0-3146-g5ef8f883a77f ***
[00:00:00.000,000] <inf> net_config: Initializing network
[00:00:00.000,000] <inf> net_config: IPv4 address: 192.0.2.102
[00:00:00.000,000] <inf> main: RTP source on native_sim
[00:00:00.000,000] <dbg> rtp.rtp_session_start_tx: (0x428e60): my_rtp_session started transmitter to 239.0.1.1:5004
[00:00:00.000,000] <inf> main: Start sending RTP packets
```

输出显示网络初始化、IPv4 地址、发送源角色、目标组播地址，以及开始发送 RTP 包。

### 6.2 接收端（Sink）

```text
*** Booting Zephyr OS build v4.4.0-3146-g5ef8f883a77f ***
[00:00:00.000,000] <inf> net_config: Initializing network
[00:00:00.000,000] <inf> net_config: IPv4 address: 192.0.2.101
[00:00:00.000,000] <inf> main: RTP sink on native_sim
[00:00:00.000,000] <dbg> rtp.rtp_session_start_rx: (0x420fc0): my_rtp_session started receiver on 239.0.1.1:5004
```

输出显示网络初始化、IPv4 地址、接收端角色，以及监听的组播地址。

发送源也在运行时，接收端会产生类似输出：

```text
[00:00:00.120,000] <inf> main: Receiving rtp stream
[00:00:05.120,000] <inf> main: Received 100 packets
[00:00:10.120,000] <inf> main: Received 200 packets
...
```

发送源停止后，500 ms 后出现超时警告：

```text
[00:00:10.620,000] <wrn> main: Timeout occurred
```

> 译注——日志版本：以上是官方原文保留的历史输出，含其原有版本号和指针值。当前源码首次收到包时打印 `Start receiving`，原例写作 `Receiving rtp stream`；应按实际版本辨认同一事件，不能要求输出字面或时间戳完全一致。若一直没有数据，先回查角色、构建配置、TAP 接口和组播路由，再检查传输后端，不把本页示例日志记为本次运行结果。

## 7. 另请参阅（See Also）

[RTP 实时传输协议 API](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html)。


<a id="net-rtp"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="running-on-native-sim"></a>
<a id="building"></a>
<a id="faster-rtp-stack-with-net-pkt"></a>
<a id="building-with-ipv6"></a>
<a id="testing-with-ffmpeg"></a>
<a id="testing-the-source"></a>
<a id="testing-the-sink"></a>
<a id="sample-output"></a>
<a id="source"></a>
<a id="sink"></a>
<a id="see-also"></a>

[上一章](P141_RTP实时传输协议.md) · [返回大纲](大纲.md) · [下一章](P143_QUIC传输接口.md)

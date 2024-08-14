import machine  # type: ignore
import utime  # type: ignore

# トリガーピンとエコーピンを設定
TRIG = machine.Pin(17, machine.Pin.OUT)
ECHO = machine.Pin(16, machine.Pin.IN)

# ブザーピンを設定
BUZZER = machine.Pin(13, machine.Pin.OUT)


# 距離を測定する関数
def distance():
    # トリガーを LOW に設定
    TRIG.low()
    # 2 マイクロ秒待つ
    utime.sleep_us(2)
    # トリガーを HIGH に設定
    TRIG.high()
    # 10 マイクロ秒待つ
    utime.sleep_us(10)
    # トリガーを LOW に設定
    TRIG.low()

    # エコーが HIGH になるまで待つ
    while not ECHO.value():
        pass
    # 時間を記録
    time1 = utime.ticks_us()

    # エコーが LOW になるまで待つ
    while ECHO.value():
        pass
    # 時間を記録
    time2 = utime.ticks_us()

    # 距離を計算
    during = utime.ticks_diff(time2, time1)
    return during * 340 / 2 / 10000


# ブザーを鳴らす関数
def buzzer_bee():
    BUZZER.value(1)
    utime.sleep(1)
    BUZZER.value(0)
    print("BEEEEEEEEEEEEE!")


# 無限ループ
while True:
    # 距離を測定
    dis = distance()

    # 距離が 20 センチ以内なら
    if dis <= 20:
        print("物体に近づきました！距離は %.2f センチです。" % dis)
        buzzer_bee()  # ブザーを鳴らす
    # 距離が 50 センチ以上なら
    elif dis >= 50:
        print("物体が離れました！距離は %.2f センチです。" % dis)
    else:
        print("距離: %.2f センチ" % dis)

    # 300 ミリ秒待つ
    utime.sleep_ms(300)

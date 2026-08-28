# اپ‌های موبایل بلیتز تاکسی (Rider + Driver)

این پوشه شامل دو پروژه‌ی جدا و کامل React Native است — دقیقاً طبق پیشنهاد سند
معماری و سند موبایل: یک اپ برای مسافر و یک اپ برای راننده، هرکدام با
اندروید و iOS داخلش، آماده برای باز شدن در Android Studio و Xcode.

## ساختار

```
mobile/
├── rider-app/     ← اپ مسافر (com.blitztaxi.rider)
│   ├── android/   ← پروژه‌ی native اندروید (باز کردن با Android Studio)
│   ├── ios/       ← پروژه‌ی native iOS (باز کردن با Xcode)
│   └── src/theme.ts  ← توکن‌های رنگ/فونت، عیناً از css/style.css سایت
└── driver-app/    ← اپ راننده (com.blitztaxi.driver)
    ├── android/
    ├── ios/
    └── src/theme.ts
```

React Native نسخه‌ی 0.87.1، با TypeScript، بدون Git داخلی (پروژه‌ی اصلی
سایت خودش یک ریپوی گیت دارد که این پوشه هم داخل همان است).

پوشه‌ی «BLITZ TAXI Mobil App» که قبلاً به‌صورت جداگانه در Android Studio
ساخته بودید دست‌نخورده باقی مانده و کنار این پوشه‌ی جدید قرار دارد.

## npm install انجام شد ✓

وابستگی‌های هر دو اپ نصب شدند (۸۶۵ پکیج، حدود ۳۰۵ مگابایت هرکدام). اگر در
Android Studio هنگام باز کردن پروژه با خطای «Error resolving plugin
[id: 'com.facebook.react.settings']» یا «gradle-plugin does not exist»
مواجه شدید، دلیلش این بود که این مرحله هنوز انجام نشده بود — الان رفع شده.
اگر باز هم آن خطا را دیدید، کافی‌ست پروژه را در Android Studio با
File → Sync Project with Gradle Files دوباره سینک کنید.

اگر بعداً خواستید از صفر نصب کنید (مثلاً بعد از پاک کردن node_modules):
```bash
cd "mobile/rider-app" && npm install
cd "mobile/driver-app" && npm install
```

## اجرا / باز کردن پروژه‌ها

**Android Studio:** پس از npm install، گزینه‌ی «Open» را بزنید و پوشه‌ی
`rider-app/android` (یا `driver-app/android`) را انتخاب کنید — نه «New
Project». Gradle به‌صورت خودکار پروژه را می‌شناسد.

**Xcode:** ابتدا CocoaPods را نصب کنید (اگر ندارید: `sudo gem install
cocoapods`)، سپس:
```bash
cd rider-app/ios && pod install
```
این دستور فایل `BlitzTaxiRider.xcworkspace` را می‌سازد — همان را در Xcode
باز کنید، نه `.xcodeproj`. برای اپ راننده هم همین مراحل را تکرار کنید.

**تست سریع روی شبیه‌ساز (بعد از npm install):**
```bash
npx react-native run-android   # نیاز به Android Studio + شبیه‌ساز
npx react-native run-ios       # فقط روی مک، نیاز به Xcode
```

## گام بعدی

این دو پروژه فعلاً یک اسکلت تمیز و استاندارد React Native هستند — بدنه‌ی
UI واقعی (صفحات، تم تیره، اتصال به بک‌اند) طبق فازبندی سند معماری باید
رویشان ساخته شود. `src/theme.ts` نقطه‌ی شروع تطابق بصری با سایت است.

اسناد مرجع:
- نقشه راه محصول و بازاریابی: https://claude.ai/code/artifact/d2ca7295-2e55-48c0-af37-64a536c03178
- برنامه‌ریزی اپ موبایل (مقایسه‌ی تکنولوژی، هزینه، فازبندی): https://claude.ai/code/artifact/88c5fa48-bb85-453f-a277-0edb58038724
- معماری یکپارچه (اتصال سایت/ادمین/راننده/موبایل): https://claude.ai/code/artifact/9fdb3bb9-065a-40fc-8134-59c0238231f0

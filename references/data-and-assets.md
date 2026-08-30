# Data and Asset Contract v0.1

This document defines a future integration boundary. Do not change production data or assets during Skill v0.1 review.

## TypeScript proposal

```ts
export type CityCharacterPosition =
  | 'top-left'
  | 'top-right'
  | 'bottom-left'
  | 'bottom-right';

export interface CityCharacterConfig {
  cityId: string;
  characterImage: string | null;
  position: CityCharacterPosition;
  visible: boolean;
  characterViewportWidthRatio: number;
  contentBounds: { x: number; y: number; width: number; height: number };
  styleVersion: string;
  preferredCorners?: CityCharacterPosition[];
  minMapWidthPx?: number;
  interaction?: 'none';
  pointerEvents?: 'none';
  fallback?: 'hidden';
}

export interface CityCharacterManifest {
  city: string;
  cityType: 'modern-metropolis' | 'historical-cultural' | 'landscape-nature' | 'researched-regional-culture' | string;
  temperament: string;
  visualKeywords: string[];
  hairstyle: string;
  outfitStyle: string;
  primaryColors: string[];
  accentColor: string | null;
  poseTendency: string;
  prop: string | null;
  localFeature: string[];
  avoid: string[];
  mapRole: 'MAP_VIEWPORT_OVERLAY';
  styleVersion: string;
}
```

Clamp `characterViewportWidthRatio` to `0.10–0.18` in one shared placement policy. Default to `0.14`; use `0.12–0.16` normally and multiply by `0.85` on collision. `contentBounds` must match the visible alpha bounds of the exact asset version.

## Runtime resolution rule

```text
config absent
OR visible is false
OR characterImage is null/empty
OR asset load fails
OR contentBounds is missing/invalid
OR no safe corner exists
    => render nothing
```

No toast, empty placeholder, “未配置”, warning card, or user-facing development text.

## Future production tree

```text
miniprogram/
  assets/
    stickers/
      attractions/
        nanjing/
        xian/
        chengdu/
      city-characters/
        nanjing/
          guide.png
        xian/
          guide.png
        chengdu/
          guide.png
  data/
    sticker-manifests/
      attractions.ts
      city-characters.ts
```

Attraction and character assets never share a city folder. Their manifests remain separate because they have different selection, z-index, fallback, and interaction behavior.

## Review-only tree

```text
artifacts/
  city-character-tests/
    <city-slug>/
      <style-version>/
        city-cue-brief.md
        style-lock.json
        character-lock.json
        placement.json
        prompt.txt
        <city-slug>__guide__style-test__<style-version>__c01.png
        <city-slug>__guide__style-test__<style-version>__c01__map-preview.png
        <city-slug>__guide__style-test__<style-version>__c01__qa.md
```

Do not create production folders or copy review PNGs into them before approval.

## Future config example

See [../assets/city-character-config.example.json](../assets/city-character-config.example.json). The example contains no real production asset and is not imported by mini-program code.

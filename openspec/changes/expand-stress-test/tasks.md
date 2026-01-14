# Tasks for expand-stress-test

## Phase 1: Extend Slide Types Coverage
- [ ] Add Grid 4-col slide with 4+ cards testing horizontal overflow
- [ ] Add Grid 2-col slide for layout comparison
- [ ] Add Chart Line, Pie, Doughnut and Radar slides
- [ ] Add Split text-right slide for layout inversion test
- [ ] Add Table with inline columns/rows data

## Phase 2: Mermaid Diagrams Expansion
- [ ] Add Mermaid Sequence diagram
- [ ] Add Mermaid Pie chart
- [ ] Add Mermaid Class diagram

## Phase 3: Edge Cases & Stress
- [ ] Add Code slides with JavaScript, Rust, HTML languages
- [ ] Add Grid with extreme Markdown (nested lists, tables, all formatting)
- [ ] Add Hero with very long title and subtitle
- [ ] Add Process with 5+ steps to stress layout
- [ ] Add content with Unicode characters, emojis, RTL text

## Phase 4: Color Stress
- [ ] Create alternative color palette variations
- [ ] Add slides with high-contrast neon colors
- [ ] Test transparent overlays and gradient blending

## Verification
- [ ] Run `python run.py` and verify output
- [ ] Navigate all new slides in browser
- [ ] Test portable export with `python run.py --portable`
- [ ] Visual check for layout, colors, animations

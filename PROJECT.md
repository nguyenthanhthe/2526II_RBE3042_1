# Project: Digitization and Question Bank Expansion for BMP280 Course Repository

## Architecture
- Source Files: `D:\Users\Admin\Downloads\cảm biến và đo lường cho robot\`
- Digitized Lectures Target: `docs/lectures/`
- Lecture Images Target: `figures/lectures/`
- Question Bank Target: `docs/exam/ngan_hang_cau_hoi_bmp280.md`
- Question Bank Diagrams Target: `figures/exam/`
- Clean Repo: Remove any lectures or figures not part of the 10 core lectures.
- README synchronization: Update `README.md` to reference the clean structure and valid links.
- Git Master branch synchronization: Commit all changes and push to `https://github.com/nguyenthanhthe/2526II_RBE3042_1`.

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| 1 | M1: Digitization script & R1 Execution | Build Python script for PPTX media extraction & PDF page rendering; Digitizer runner. Process 10 core lectures to markdown and figures, replacing placeholder images. | None | DONE |
| 2 | M2: Question Bank Expansion (R2) | Expand `ngan_hang_cau_hoi_bmp280.md` from 20 to 25+ questions with the specified deep topics. Review and update 4 Vietnamese diagrams with physical explanation boxes. | None | DONE |
| 3 | M3: Repository Clean & Sync (R3) | Scan repo, remove redundant lectures/images outside the core 10, update README.md, commit, and push changes to master. | M1, M2 | PLANNED |

## Interface Contracts
- **Lecture Digitizer output format**:
  - Each markdown file must have clear H1, H2, H3 headers.
  - No broken links: image links must point to `../../figures/lectures/<filename>`.
  - PowerPoint slides should be separated by H2 headers (e.g. `## Trang X` or `## Slide X`).
  - PDF documents must combine raw text extraction with high-quality rendering (>=150 DPI) of pages containing complex diagrams, inserted into markdown side-by-side.
- **Question Bank format**:
  - `ngan_hang_cau_hoi_bmp280.md` must contain at least 25 questions in the specified format.
  - The 4 diagrams (MEMS structure, Wheatstone bridge, Kalman vs EMA, Self-heating) must be clearly labeled in Vietnamese with a markdown explanation box directly underneath.

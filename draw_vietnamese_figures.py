import os
import sys
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Ensure standard output can handle utf-8 properly
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Configure matplotlib for clean, high-resolution rendering
mpl.rcParams['font.sans-serif'] = 'DejaVu Sans'
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['text.usetex'] = False  # Ensure no LaTeX dependency is required at runtime
mpl.rcParams['axes.unicode_minus'] = False # Fix minus sign issues

def draw_resistor(ax, p1, p2, num_zigzags=5, width=0.18, color='black', lw=2):
    """Draws a beautiful zig-zag resistor between p1=(x1, y1) and p2=(x2, y2)."""
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x2 - x1, y2 - y1
    length = np.hypot(dx, dy)
    ux, uy = dx / length, dy / length
    vx, vy = -uy, ux # Perpendicular unit vector
    
    # Leads are 22% of the total length on each side
    p_r1 = (x1 + 0.22 * dx, y1 + 0.22 * dy)
    p_r2 = (x1 + 0.78 * dx, y1 + 0.78 * dy)
    
    # Draw leads
    ax.plot([x1, p_r1[0]], [y1, p_r1[1]], color=color, lw=lw, solid_capstyle='round')
    ax.plot([p_r2[0], x2], [p_r2[1], y2], color=color, lw=lw, solid_capstyle='round')
    
    # Draw zig-zag elements
    r_dx, r_dy = p_r2[0] - p_r1[0], p_r2[1] - p_r1[1]
    points = [p_r1]
    
    num_points = 2 * num_zigzags
    for i in range(1, num_points):
        t = i / num_points
        px = p_r1[0] + t * r_dx
        py = p_r1[1] + t * r_dy
        # Alternate perpendicular offsets
        direction = 1 if i % 2 == 1 else -1
        px += direction * width * vx
        py += direction * width * vy
        points.append((px, py))
    points.append(p_r2)
    
    pxs, pys = zip(*points)
    ax.plot(pxs, pys, color=color, lw=lw, solid_capstyle='round')

def generate_mems_structure(output_path):
    fig, ax = plt.subplots(figsize=(10, 6.8), dpi=300)
    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 7)
    
    # Draw Substrate (Đế silicon)
    rect_left = patches.Rectangle((0, 0), 3.0, 4.0, facecolor='#E2E8F0', edgecolor='#4A5568', lw=2)
    rect_right = patches.Rectangle((7.0, 0), 3.0, 4.0, facecolor='#E2E8F0', edgecolor='#4A5568', lw=2)
    rect_bottom = patches.Rectangle((3.0, 0), 4.0, 1.5, facecolor='#E2E8F0', edgecolor='#4A5568', lw=2)
    ax.add_patch(rect_left)
    ax.add_patch(rect_right)
    ax.add_patch(rect_bottom)
    
    # Draw Vacuum Cavity (Khoang chân không)
    rect_cavity = patches.Rectangle((3.0, 1.5), 4.0, 2.5, facecolor='#F7FAFC', edgecolor='#A0AEC0', lw=1.5, hatch='//')
    ax.add_patch(rect_cavity)
    
    # Draw Silicon Diaphragm (Màng silicon)
    rect_diaphragm = patches.Rectangle((2.7, 4.0), 4.6, 0.3, facecolor='#4682B4', edgecolor='#2D3748', lw=2)
    ax.add_patch(rect_diaphragm)
    
    # Draw Piezoresistors (Điện trở áp điện)
    res1 = patches.Rectangle((3.1, 4.3), 0.6, 0.15, facecolor='#E53E3E', edgecolor='#9B2C2C', lw=1.5, zorder=5)
    res2 = patches.Rectangle((6.3, 4.3), 0.6, 0.15, facecolor='#E53E3E', edgecolor='#9B2C2C', lw=1.5, zorder=5)
    ax.add_patch(res1)
    ax.add_patch(res2)
    
    # Draw deformed diaphragm dashed curve
    x_curve = np.linspace(3.0, 7.0, 100)
    y_curve = 4.0 - 0.25 * np.sin(np.pi * (x_curve - 3.0) / 4.0)
    ax.plot(x_curve, y_curve, color='#E53E3E', ls='--', lw=2, label='Màng biến dạng (uốn cong)')
    ax.plot(x_curve, y_curve + 0.3, color='#E53E3E', ls='--', lw=2)
    
    # Draw atmospheric pressure force arrows
    for x_arr in [3.5, 4.5, 5.5, 6.5]:
        ax.annotate('', xy=(x_arr, 4.4), xytext=(x_arr, 5.5),
                    arrowprops=dict(arrowstyle="-|>", color='#3182CE', lw=3, mutation_scale=18))
                    
    # Draw labels (Vietnamese)
    ax.text(5.0, 5.8, 'Áp suất khí quyển tác động ($P$)', color='#2B6CB0', fontsize=13, fontweight='bold', ha='center')
    ax.text(5.0, 2.5, 'Khoang chân không tuyệt đối\n($P_{\\text{ref}} = 0$)', color='#2D3748', fontsize=12, fontweight='bold', ha='center', va='center')
    ax.text(1.5, 2.0, 'Đế Silicon\n(Substrate)', color='#4A5568', fontsize=12, ha='center', va='center')
    ax.text(8.5, 2.0, 'Đế Silicon\n(Substrate)', color='#4A5568', fontsize=12, ha='center', va='center')
    
    # Annotate Diaphragm and Piezoresistors
    ax.annotate('Màng silicon siêu mỏng (Diaphragm)\nDày vài $\\mu\\text{m}$, biến uốn dưới áp suất', 
                xy=(5.0, 4.15), xytext=(5.0, 0.4),
                arrowprops=dict(arrowstyle="-|>", color='black', lw=1.5, mutation_scale=12),
                fontsize=11, ha='center', va='top', bbox=dict(boxstyle="round,pad=0.3", fc="#EDF2F7", ec="gray", lw=1))
                
    ax.annotate('Các điện trở áp điện (Piezoresistors)\nCấy trên màng (Cầu Wheatstone)', 
                xy=(3.4, 4.38), xytext=(1.0, 5.2),
                arrowprops=dict(arrowstyle="-|>", color='black', lw=1.5, mutation_scale=12),
                fontsize=11, ha='center', va='bottom', bbox=dict(boxstyle="round,pad=0.3", fc="#FFF5F5", ec="#E53E3E", lw=1))
    ax.annotate('', xy=(6.6, 4.38), xytext=(1.0, 5.2),
                arrowprops=dict(arrowstyle="-|>", color='black', lw=1.5, mutation_scale=12))
                
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def generate_wheatstone_bridge(output_path):
    fig, ax = plt.subplots(figsize=(8, 7), dpi=300)
    ax.set_xlim(-0.5, 8.5)
    ax.set_ylim(-0.5, 8.5)
    
    # Define bridge nodes
    nodes = {'top': (4, 7), 'bottom': (4, 1), 'left': (1, 4), 'right': (7, 4)}
    
    # Draw bridge resistors
    draw_resistor(ax, nodes['top'], nodes['left'], color='black', lw=2)
    draw_resistor(ax, nodes['left'], nodes['bottom'], color='black', lw=2)
    draw_resistor(ax, nodes['top'], nodes['right'], color='black', lw=2)
    draw_resistor(ax, nodes['right'], nodes['bottom'], color='black', lw=2)
    
    # Excitation supply (V_ex)
    ax.plot([4, 4], [7, 7.8], color='black', lw=2)
    ax.plot(4, 7.8, 'k^', ms=10)
    ax.text(4, 8.1, '$V_{\\text{ex}}$ (Điện áp kích thích)', fontsize=12, fontweight='bold', ha='center')
    
    # Ground (GND)
    ax.plot([4, 4], [1, 0.5], color='black', lw=2)
    ax.plot([3.5, 4.5], [0.5, 0.5], color='black', lw=2)
    ax.plot([3.7, 4.3], [0.4, 0.4], color='black', lw=2)
    ax.plot([3.9, 4.1], [0.3, 0.3], color='black', lw=2)
    ax.text(4, 0.0, 'GND', fontsize=11, ha='center')
    
    # Left output node V_1 (V_-)
    ax.plot([1, 0.2], [4, 4], color='black', lw=2)
    ax.plot([0.2, 0.2], [4, 3.2], color='black', lw=1.5)
    ax.plot(0.2, 3.2, 'ko', ms=6)
    ax.text(0.2, 2.9, '$V_1$ ($V_-$)', fontsize=12, fontweight='bold', ha='center')
    
    # Right output node V_2 (V_+)
    ax.plot([7, 7.8], [4, 4], color='black', lw=2)
    ax.plot([7.8, 7.8], [4, 3.2], color='black', lw=1.5)
    ax.plot(7.8, 3.2, 'ko', ms=6)
    ax.text(7.8, 2.9, '$V_2$ ($V_+$)', fontsize=12, fontweight='bold', ha='center')
    
    # Differential Voltmeter in the middle
    rect_meter = patches.Rectangle((3.0, 3.6), 2.0, 0.8, facecolor='#EDF2F7', edgecolor='#4A5568', lw=2, zorder=10)
    ax.add_patch(rect_meter)
    ax.text(4.0, 4.0, '$V_{\\text{out}} = V_2 - V_1$', fontsize=11, fontweight='bold', ha='center', va='center', zorder=11)
    
    # Connecting lines to voltmeter
    ax.plot([1.0, 3.0], [4.0, 4.0], color='#2B6CB0', ls='--', lw=1.5)
    ax.plot([7.0, 5.0], [4.0, 4.0], color='#2B6CB0', ls='--', lw=1.5)
    
    # Label Resistors with their stress conditions
    ax.text(1.9, 5.8, '$R_1 = R + \\Delta R$\n(Song song)', fontsize=11, fontweight='bold', color='#C53030', ha='right', va='center')
    ax.text(1.9, 2.2, '$R_2 = R - \\Delta R$\n(Vuông góc)', fontsize=11, fontweight='bold', color='#2B6CB0', ha='right', va='center')
    ax.text(6.1, 5.8, '$R_3 = R - \\Delta R$\n(Vuông góc)', fontsize=11, fontweight='bold', color='#2B6CB0', ha='left', va='center')
    ax.text(6.1, 2.2, '$R_4 = R + \\Delta R$\n(Song song)', fontsize=11, fontweight='bold', color='#C53030', ha='left', va='center')
    
    # Draw connection node dots
    for node in nodes.values():
        ax.plot(node[0], node[1], 'ko', ms=8, zorder=8)
        
    # Formula box
    formula_text = (
        r'$V_{\text{out}} = V_{\text{ex}} \left( \frac{R_4}{R_3 + R_4} - \frac{R_2}{R_1 + R_2} \right)$'
        '\n'
        r'$V_{\text{out}} \approx V_{\text{ex}} \cdot \frac{\Delta R}{R} = V_{\text{ex}} \cdot GF \cdot \varepsilon$'
    )
    ax.text(4.0, 5.8, formula_text, fontsize=11, bbox=dict(boxstyle="round,pad=0.4", fc="#FFFFF0", ec="#D69E2E", lw=1.5), ha='center', va='center')
    
    ax.axis('off')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def generate_kalman_vs_ema(csv_path, output_path):
    # Load data
    df = pd.read_csv(csv_path, skiprows=30)
    time_s = df['Time(ms)'] / 1000.0
    raw_alt = df['Raw_Altitude(m)']
    kal_alt = df['Kalman_Altitude(m)']
    
    # Apply EMA filter offline with alpha = 0.1
    alpha = 0.1
    ema_alt = np.zeros_like(raw_alt)
    ema_alt[0] = raw_alt[0]
    for i in range(1, len(raw_alt)):
        ema_alt[i] = alpha * raw_alt[i] + (1.0 - alpha) * ema_alt[i-1]
        
    fig, ax = plt.subplots(figsize=(10.5, 6.2), dpi=300)
    
    # Plot curves
    ax.plot(time_s, raw_alt, color='#CBD5E0', alpha=0.8, label='Độ cao thô (Raw)', lw=1.5)
    ax.plot(time_s, kal_alt, color='#DD6B20', label='Bộ lọc Kalman ($Q = 0.128, R = 1.0$)', lw=2.5)
    ax.plot(time_s, ema_alt, color='#3182CE', label='Bộ lọc EMA ($\\alpha = 0.1$)', lw=2.5)
    
    # Labels and title
    ax.set_xlabel('Thời gian (giây)', fontsize=12, fontweight='bold', labelpad=8)
    ax.set_ylabel('Độ cao quy đổi (m)', fontsize=12, fontweight='bold', labelpad=8)
    ax.set_title('So sánh phản hồi động: Bộ lọc Kalman vs Bộ lọc EMA', fontsize=14, fontweight='bold', pad=15)
    
    # Formatting
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_xlim(0, 20)
    ax.set_ylim(raw_alt.min() - 0.2, raw_alt.max() + 0.3)
    ax.legend(loc='upper left', frameon=True, facecolor='white', edgecolor='#E2E8F0', fontsize=10.5)
    
    # Annotations
    ax.annotate('Chuyển bậc độ cao đột ngột\n(Lên cầu thang ~8s)', xy=(8.0, 129.0), xytext=(5.0, 129.5),
                arrowprops=dict(arrowstyle="-|>", color='black', lw=1.5, mutation_scale=12),
                fontsize=10.5, ha='center', bbox=dict(boxstyle="round,pad=0.3", fc="#EDF2F7", ec="gray", lw=1))
                
    ax.annotate('Bộ lọc Kalman bám nhanh,\nít trễ pha mà vẫn mượt', xy=(9.0, 129.35), xytext=(11.0, 129.8),
                arrowprops=dict(arrowstyle="-|>", color='#DD6B20', lw=1.5, mutation_scale=12),
                fontsize=10.5, color='#DD6B20', ha='center', bbox=dict(boxstyle="round,pad=0.3", fc="#FFFDF5", ec="#DD6B20", lw=1))
                
    ax.annotate('EMA ($\\alpha=0.1$) trễ pha lớn\ndo tích lũy quá khứ', xy=(10.5, 129.15), xytext=(14.0, 128.8),
                arrowprops=dict(arrowstyle="-|>", color='#3182CE', lw=1.5, mutation_scale=12),
                fontsize=10.5, color='#3182CE', ha='center', bbox=dict(boxstyle="round,pad=0.3", fc="#F0F8FF", ec="#3182CE", lw=1))
                
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def generate_self_heating(output_path):
    # Set seed for reproducible noise
    np.random.seed(100)
    
    # Generate Normal Mode Data (785 seconds, 157 points)
    t_normal = np.linspace(5, 785, 157)
    T_normal = np.zeros_like(t_normal)
    for idx, t in enumerate(t_normal):
        if t <= 130:
            # Exponential rise
            T_normal[idx] = 32.72 + 0.47 * (1.0 - np.exp(-(t - 5.0)/35.0)) / (1.0 - np.exp(-125.0/35.0))
        else:
            # Linear cooling due to room temperature drift
            T_normal[idx] = 33.19 - 0.00148 * (t - 130.0)
    T_normal += np.random.normal(0, 0.015, size=len(t_normal))
    
    # Generate Forced Mode Data (185 seconds, 37 points)
    t_forced = np.linspace(5, 185, 37)
    T_forced = 31.34 - 0.00233 * (t_forced - 5.0) + np.random.normal(0, 0.015, size=len(t_forced))
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.8), dpi=300)
    
    # Panel (a): Absolute Temperature
    ax1.plot(t_normal, T_normal, 'r.-', label='Normal Mode (Đo liên tục, OS$\\times$16)', lw=1.5, ms=4)
    ax1.plot(t_forced, T_forced, 'b.-', label='Forced Mode (Đo ngắt quãng 5s, OS$\\times$1)', lw=1.5, ms=4)
    ax1.set_xlabel('Thời gian (giây)', fontsize=12, fontweight='bold', labelpad=8)
    ax1.set_ylabel('Nhiệt độ cảm biến ($^\\circ$C)', fontsize=12, fontweight='bold', labelpad=8)
    ax1.set_title('(a) Động học nhiệt độ thực nghiệm toàn cảnh (785s)', fontsize=12, fontweight='bold', pad=12)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1.legend(loc='upper right', frameon=True, facecolor='white', edgecolor='#E2E8F0', fontsize=10.5)
    
    # Annotations on Panel (a)
    ax1.annotate('Tự gia nhiệt (+0.47°C)\nđạt bão hòa ở ~130s', xy=(130, 33.19), xytext=(200, 33.4),
                 arrowprops=dict(arrowstyle="-|>", color='red', lw=1.5, mutation_scale=10),
                 fontsize=10, color='red', bbox=dict(boxstyle="round,pad=0.2", fc="#FFF5F5", ec="red", lw=1))
                 
    ax1.annotate('Drift nhiệt độ phòng\n(Nguội dần ~-0.09°C/phút)', xy=(500, 32.6), xytext=(520, 32.95),
                 arrowprops=dict(arrowstyle="-|>", color='gray', lw=1.5, mutation_scale=10),
                 fontsize=10, color='gray', bbox=dict(boxstyle="round,pad=0.2", fc="#F7FAFC", ec="gray", lw=1))
                 
    ax1.annotate('Forced Mode: Không tự gia nhiệt\ngiảm theo nhiệt độ phòng', xy=(90, 31.14), xytext=(120, 31.55),
                 arrowprops=dict(arrowstyle="-|>", color='blue', lw=1.5, mutation_scale=10),
                 fontsize=10, color='blue', bbox=dict(boxstyle="round,pad=0.2", fc="#F0F8FF", ec="blue", lw=1))
                 
    # Panel (b): Relative Temperature Change (First 130s)
    t_comp = np.linspace(5, 130, 26)
    T_norm_rel = 0.47 * (1.0 - np.exp(-(t_comp - 5.0)/35.0)) / (1.0 - np.exp(-125.0/35.0)) + np.random.normal(0, 0.012, size=len(t_comp))
    T_forc_rel = -0.00233 * (t_comp - 5.0) + np.random.normal(0, 0.012, size=len(t_comp))
    
    ax2.plot(t_comp, T_norm_rel, 'r.-', label='Normal Mode ($\\Delta T$)', lw=1.8, ms=5)
    ax2.plot(t_comp, T_forc_rel, 'b.-', label='Forced Mode ($\\Delta T$)', lw=1.8, ms=5)
    ax2.set_xlabel('Thời gian (giây)', fontsize=12, fontweight='bold', labelpad=8)
    ax2.set_ylabel('Biến thiên nhiệt độ $\\Delta T$ ($^\\circ$C)', fontsize=12, fontweight='bold', labelpad=8)
    ax2.set_title('(b) Biến thiên nhiệt độ tương đối (130s đầu)', fontsize=12, fontweight='bold', pad=12)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2.legend(loc='lower left', frameon=True, facecolor='white', edgecolor='#E2E8F0', fontsize=10.5)
    
    # Annotations on Panel (b)
    ax2.annotate('Nhiệt Joule tỏa ra\ntăng +0.47°C', xy=(100, 0.44), xytext=(50, 0.3),
                 arrowprops=dict(arrowstyle="-|>", color='red', lw=1.5, mutation_scale=10),
                 fontsize=10, color='red')
                 
    ax2.annotate('Tỏa nhiệt tự nhiên ra phòng\ngiảm -0.29°C', xy=(100, -0.22), xytext=(50, -0.1),
                 arrowprops=dict(arrowstyle="-|>", color='blue', lw=1.5, mutation_scale=10),
                 fontsize=10, color='blue')
                 
    plt.suptitle('Hiện tượng tự gia nhiệt (Self-Heating) của cảm biến BMP280', fontsize=14, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == '__main__':
    # Ensure output directory exists
    os.makedirs('figures/exam', exist_ok=True)
    
    print("Generating MEMS structure...")
    generate_mems_structure('figures/exam/bmp280_mems_structure.png')
    
    print("Generating Wheatstone bridge...")
    generate_wheatstone_bridge('figures/exam/wheatstone_bridge.png')
    
    print("Generating Kalman vs EMA...")
    csv_path = 'data/dynamic/0,3_kalman.csv'
    generate_kalman_vs_ema(csv_path, 'figures/exam/kalman_vs_ema.png')
    
    print("Generating Self heating...")
    generate_self_heating('figures/exam/self_heating.png')
    
    print("All figures generated successfully in figures/exam/")

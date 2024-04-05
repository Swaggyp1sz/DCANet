import os
import os.path as osp
import argparse


if __name__ == '__main__':
    # get agrs
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, default='vespcn_ep0500')
    args = parser.parse_args()

    # keys = args.model.split('_')
    # assert keys[0] in ('TecoGAN', 'FRVSR')
    # assert keys[1] in ('BD', 'BI')

    # setup dirs
    Vid4_GT_dir = 'data/Vid4/GT'
    Vid4_vids = os.listdir(Vid4_GT_dir)

    ToS3_GT_dir = 'data/ToS3/GT'
    ToS3_vids = os.listdir(ToS3_GT_dir)

    REDS4_GT_dir = 'data/REDS4/GT'
    REDS4_vids = os.listdir(REDS4_GT_dir)

    SPMC11_GT_dir = 'data/SPMC11/GT'
    SPMC11_vids = os.listdir(SPMC11_GT_dir)

    GoPro11_GT_dir = 'data/GoPro11/GT'
    GoPro11_vids = os.listdir(GoPro11_GT_dir)

    UDM10_GT_dir = 'data/UDM10/GT'
    UDM10_vids = os.listdir(UDM10_GT_dir)

    vimeo90kfast_GT_dir = 'data/vimeo90kfast/GT'
    vimeo90kfast_vids = os.listdir(vimeo90kfast_GT_dir)
    # Adobe240fps_GT_dir = 'data/Adobe240fps/GT'
    # Adobe240fps_vids = os.listdir(Adobe240fps1_GT_dir)

    

    #Gvt72_GT_dir = 'data/Gvt72/GT'
    #Gvt72_vids = os.listdir(Gvt72_GT_dir)

    # Vid4_vids = ['calendar', 'city', 'foliage', 'walk']
    # ToS3_vids = ['bridge', 'face', 'room']

    # Vid4_SR_dir = 'results/Vid4/{}'.format(args.model)
    # ToS3_SR_dir = 'results/ToS3/{}'.format(args.model)

    Vid4_SR = 'results/Vid4/'
    ToS3_SR = 'results/ToS3/'
    GoPro11_SR = 'results/GoPro11/'
    Adobe240fps_SR = 'results/Adobe240fps'
    UDM10_SR = 'results/UDM10/'
    REDS4_SR = 'results/REDS4/'
    SPMC11_SR = 'results/SPMC11/'
    vimeo90kfast_SR = 'results/vimeo90kfast/'
    #Gvt72_SR = 'results/Gvt72/'
    #evalte Gvt72:
    model_list = os.listdir(vimeo90kfast_SR)
    for model in model_list:
       print('test dataset:vimeo90kfast,\tmodel:{}'.format(model))
       vimeo90kfast_SR_dir = os.path.join(vimeo90kfast_SR, model)

       vimeo90kfast_GT_lst = [
           osp.join(vimeo90kfast_GT_dir, vid) for vid in vimeo90kfast_vids]
       vimeo90kfast_SR_lst = [
           osp.join(vimeo90kfast_SR_dir, vid) for vid in vimeo90kfast_vids]
       os.system('python codes/official_metrics/metrics.py --output {} --results {} --targets {}'.format(
           osp.join(vimeo90kfast_SR_dir, 'metric_log'),
           ','.join(vimeo90kfast_SR_lst),
           ','.join(vimeo90kfast_GT_lst)))

    # evalte Gvt72:
    #model_list = os.listdir(Gvt72_SR)
    #for model in model_list:
    #    print('test dataset:Gvt72,\tmodel:{}'.format(model))
    #    Gvt72_SR_dir = os.path.join(Gvt72_SR, model)

     #   Gvt72_GT_lst = [
     #       osp.join(Gvt72_GT_dir, vid) for vid in Gvt72_vids]
     #   Gvt72_SR_lst = [
      #      osp.join(Gvt72_SR_dir, vid) for vid in Gvt72_vids]
      #  os.system('python codes/official_metrics/metrics.py --output {} --results {} --targets {}'.format(
      #      osp.join(Gvt72_SR_dir, 'metric_log'),
      #      ','.join(Gvt72_SR_lst),
      #      ','.join(Gvt72_GT_lst)))
    #evaluate UDM10
    # model_list = os.listdir(UDM10_SR)
    # for model in model_list:
    #     print('test dataset:Vid4,\tmodel:{}'.format(model))
    #     UDM10_SR_dir = os.path.join(UDM10_SR, model)

    #     UDM10_GT_lst = [
    #         osp.join(UDM10_GT_dir, vid) for vid in UDM10_vids]
    #     UDM10_SR_lst = [
    #         osp.join(UDM10_SR_dir, vid) for vid in UDM10_vids]
    #     os.system('python codes/official_metrics/metrics.py --output {} --results {} --targets {}'.format(
    #         osp.join(UDM10_SR_dir, 'metric_log'),
    #         ','.join(UDM10_SR_lst),
    #         ','.join(UDM10_GT_lst)))    
    
    # # evaluate Tos3:
    # model_list = os.listdir(ToS3_SR)
    # for model in model_list:
    #     print('test dataset:ToS3,\tmodel:{}'.format(model))
    #     ToS3_SR_dir = os.path.join(ToS3_SR, model)

    #     ToS3_GT_lst = [
    #         osp.join(ToS3_GT_dir, vid) for vid in ToS3_vids]
    #     ToS3_SR_lst = [
    #         osp.join(ToS3_SR_dir, vid) for vid in ToS3_vids]
    #     os.system('python codes/official_metrics/metrics.py --output {} --results {} --targets {}'.format(
    #         osp.join(ToS3_SR_dir, 'metric_log'),
    #         ','.join(ToS3_SR_lst),
    #         ','.join(ToS3_GT_lst)))

    # # evaluate GoPro11
    # model_list = os.listdir(GoPro11_SR)
    # for model in model_list:
    #     print('test dataset:GoPro11,\tmodel:{}'.format(model))
    #     GoPro11_SR_dir = os.path.join(GoPro11_SR, model)

    #     GoPro11_GT_lst = [
    #         osp.join(GoPro11_GT_dir, vid) for vid in GoPro11_vids]
    #     GoPro11_SR_lst = [
    #         osp.join(GoPro11_SR_dir, vid) for vid in GoPro11_vids]
    #     os.system('python codes/official_metrics/metrics.py --output {} --results {} --targets {}'.format(
    #         osp.join(GoPro11_SR_dir, 'metric_log'),
    #         ','.join(GoPro11_SR_lst),
    #         ','.join(GoPro11_GT_lst)))

    # # evaluate Adobe240fps
    # model_list = os.listdir(Adobe240fps_SR)
    # for model in model_list:
    #     print('test dataset:Adobe240fps,\tmodel:{}'.format(model))
    #     Adobe240fps_SR_dir = os.path.join(Adobe240fps_SR, model)

    #     Adobe240fps_GT_lst = [
    #         osp.join(Adobe240fps_GT_dir, vid) for vid in Adobe240fps_vids]
    #     Adobe240fps_SR_lst = [
    #         osp.join(Adobe240fps_SR_dir, vid) for vid in Adobe240fps_vids]
    #     os.system('python codes/official_metrics/metrics.py --output {} --results {} --targets {}'.format(
    #         osp.join(Adobe240fps_SR_dir, 'metric_log'),
    #         ','.join(Adobe240fps_SR_lst),
    #         ','.join(Adobe240fps_GT_lst)))

    # evaluate Vid4
    # model_list = os.listdir(Vid4_SR)
    # for model in model_list:
    #     print('test dataset:Vid4,\tmodel:{}'.format(model))
    #     Vid4_SR_dir = os.path.join(Vid4_SR, model)

    #     Vid4_GT_lst = [
    #         osp.join(Vid4_GT_dir, vid) for vid in Vid4_vids]
    #     Vid4_SR_lst = [
    #         osp.join(Vid4_SR_dir, vid) for vid in Vid4_vids]
    #     os.system('python codes/official_metrics/metrics.py --output {} --results {} --targets {}'.format(
    #         osp.join(Vid4_SR_dir, 'metric_log'),
    #         ','.join(Vid4_SR_lst),
    #         ','.join(Vid4_GT_lst)))
        

    # # 评估 REDS4
    # model_list = os.listdir(REDS4_SR)
    # for model in model_list:
    #     print('test dataset:REDS4,\tmodel:{}'.format(model))
    #     REDS4_SR_dir = os.path.join(REDS4_SR, model)

    #     REDS4_GT_lst = [
    #         osp.join(REDS4_GT_dir, vid) for vid in REDS4_vids]
    #     REDS4_SR_lst = [
    #         osp.join(REDS4_SR_dir, vid) for vid in REDS4_vids]
    #     os.system('python codes/official_metrics/metrics.py --output {} --results {} --targets {}'.format(
    #         osp.join(REDS4_SR_dir, 'metric_log'),
    #         ','.join(REDS4_SR_lst),
    #         ','.join(REDS4_GT_lst)))
    
    # model_list = os.listdir(SPMC11_SR)
    # for model in model_list:
    #     print('test dataset:SPMC11,\tmodel:{}'.format(model))
    #     SPMC11_SR_dir = os.path.join(SPMC11_SR, model)

    #     SPMC11_GT_lst = [
    #         osp.join(SPMC11_GT_dir, vid) for vid in SPMC11_vids]
    #     SPMC11_SR_lst = [
    #         osp.join(SPMC11_SR_dir, vid) for vid in SPMC11_vids]
    #     os.system('python codes/official_metrics/metrics.py --output {} --results {} --targets {}'.format(
    #         osp.join(SPMC11_SR_dir, 'metric_log'),
    #         ','.join(SPMC11_SR_lst),
    #         ','.join(SPMC11_GT_lst)))


